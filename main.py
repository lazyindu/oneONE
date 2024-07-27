import subprocess

def start_bot(script_name):
    return subprocess.Popen(["python3", script_name])

if __name__ == '__main__':
    # Start individual bot scripts
    processes = [
        start_bot("bot_0.py"),
        start_bot("bot_1.py")
    ]

    # Wait for all processes to complete
    for process in processes:
        process.wait()
