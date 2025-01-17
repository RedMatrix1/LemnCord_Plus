import os
import subprocess

commands = {
    "send message": "send_message.py",
    "leave server": "leave_server.py",
    "get channels": "get_channels.py",
    "get servers": "get_servers.py",
}

root_directory = os.getcwd()

def execute_command(command):
    script_path = os.path.join(root_directory, "commands", command)
    subprocess.run(["python3", script_path])

while True:
    menu = input('Command(check listofcommands.txt): ')

    if menu in commands:
        execute_command(commands[menu])
    else:
        print("Invalid command.")
