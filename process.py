import psutil
import time

command_names = ['docker', 'top']

def check_process(command_names):
    for command_name in command_names:
        found =False
        for process in psutil.process_iter(attrs=['cmdline']):
            cmd_line = process.info.get('cmdline')
            if cmd_line and command_name in cmd_line:
                found = True
                break
        if found:
            print(f"Process '{command_name}' is running.")
        else:
            print(f"Process '{command_name}' is not running. Taking action ...")

if __name__ == "__main__":
    while True:
        check_process(command_names)
        time.sleep(30)