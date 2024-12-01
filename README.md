# Dolphin
Dolphin Command and Control Framework  

This repository contains a modular Python-based framework designed for advanced system interaction, scripting, and remote management via webhooks. It provides utilities to create and manage scripts, gather system information, execute commands, and establish remote control mechanisms using Flask-based APIs and webhook integrations. The framework includes a dynamic menu system and a lightweight backdoor integration feature for testing purposes.

# Features:
Menu-Driven Interface:

Interactive command-line menu for managing scripts and executing tasks.
Options for running terminal scripts, creating worker scripts, and clearing script records.
# Worker Script Automation:

Auto-generates worker scripts with user-defined parameters (script name, username, webhook URL).
Integrates webhook functionality to report system information and updates.
# Ngrok Integration:

Automates the setup of Ngrok tunnels for secure public URLs.
Retrieves system and network information (local/public IP, system details).
# Remote Command Execution:

Accepts and executes system commands via a Flask-based API.
Supports directory changes, Python script execution, and command output retrieval.
# System Information Gathering:

Collects comprehensive system and IP-related details.
Reports data via JSON to a webhook for easy monitoring.
# Backdoor Injection Tool:

Provides functionality to append backdoor scripts to existing Python files for testing.
# Cross-Platform Support:

Works seamlessly on Linux and Windows systems.

# Dependencies:
Flask for API handling.
requests for HTTP requests.
dhooks for Discord webhook interaction.
subprocess and os for system-level command execution.
# Use Cases:
Penetration testing and ethical hacking experiments.
Remote script management and testing in controlled environments.
Quick system information gathering for monitoring and debugging.
# Note: Use this tool responsibly and only in environments where you have explicit permission. This project is for educational and research purposes only. Misuse of the tool may result in legal consequences.
