# DaemonKit

## Introduction
DaemonKit is a Python toolkit for creating and managing daemon processes. It simplifies the process of daemon creation, which involves running tasks in the background independently of user sessions, typically without a user interface. To create a daemon, simply integrate your script logic into the `user_task` function in the `daemon_template.py` template, transforming standard Python scripts into background-running daemons.

## Features
- Simplifies the creation and management of daemon processes in Python.
- Allows for customizable behavior across different daemon tasks.
- Provides efficient logging, error handling, and PID file management.


## Installation
Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/AlmaStreet/daemonkit.git
cd daemonkit
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python setup.py install
```

## Configuration
Before running the examples, configure the `output_dir` in the `.settings` file:
```
[DEFAULT]
output_dir = ~/repos/daemon_practice
```
Replace output_dir with the desired path for daemon outputs.


## Daemon Examples
### helloworld.py
Creates a daemon to save "Hello World" to `daemon_output.txt` and saves the process id to `daemon_pid.txt`
### monitor_logs.py
Monitors the current directory for any file creations and logs the activity to daemon_logs.txt. Test this by creating a file in the directory:
```
touch text_file.txt
```

## Daemon Template
Create your own daemon processes using `daemon_template.py`. Include the tasks you want to run in the `user_task()` function:
```
from daemon_creator.daemon import Daemon


def user_task():
    # User's specific task logic
    message = "Performing my task..."
    my_daemon.log_task_output(message)


if __name__ == "__main__":
    daemon_name = "daemon_template"
    my_daemon = Daemon(name=daemon_name, task_function=user_task)
    my_daemon.start()

```

Start the daemon with:
```
python3 template/daemon_template.py
```

## Daemon Management Service
Use the daemon management service to view currently running daemons and terminate specific or all daemons.

Example with no daemons running:
```
% python3 manage_daemon.py                                  
No daemons are currently running.
```

Example with a running daemon:
```
% python3 manage_daemon.py                
1) daemon_template
Select a daemon to stop (or 0 to stop all): 1
Stopped daemon 'daemon_template' with PID 63821.
```

## Slaying the daemon
Apart from using the Daemon Management Service, you can manually terminate daemons. Retrieve the process ID (PID) from `daemon_pid.txt`.
### UI
Open the Activity Monitor app and look for a Python or Python3 process with the same PID as the daemon. Terminate the process by clicking on it and then clicking the 'X'.
### CLI
Terminate the daemon using:
```
kill <daemon pid>
```
Replace <daemon_pid> with the actual PID of the daemon.