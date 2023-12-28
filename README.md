# daemon_practice

## Introduction
This repo contains 2 scripts to create daemons to perform different tasks.
We are creating a daemon, which is a process that runs in the background and not directly under out control. They typically don't have a UI and run independently of user sessions.

## Installation
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## What the script does
### helloworldd.py
Creates a daemon to save "Hello World" to daemon_output.txt
Also saves its process id to daemon_pid.txt
### monitor_logsd.py
This daemon will monitor the current directory for any any file creations and save the activity to daemon_logs.txt.
You can test this by creating a file in the directory using `touch text_file.txt`

## Slaying the daemon
To kill the daemon process, get the process id (pid) from the daemon_pid.txt file.
### UI
Open Activity Monitor app and look for a Python or Python3 process.
One of the process will have the same pid as our daemon pid.
Click the process and click the x to kill the process.
### CLI
```kill <daemon pid>```
