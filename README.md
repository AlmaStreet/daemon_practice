# DaemonKit

## Introduction
DaemonKit is a Python toolkit for creating and managing daemon processes. It simplifies the process of daemon creation, which involves running tasks in the background independently of user sessions, typically without a user interface. With DaemonKit, you can easily transform standard Python scripts into background-running daemons by integrating your script logic into the provided template.

## Features
- Simplifies the creation and management of daemon processes in Python.
- Allows for customizable behavior across different daemon tasks.
- Provides efficient logging, error handling, and PID (Process ID) file management.


## Installation
To get started with DaemonKit, follow these installation steps:

```
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
output_dir = ~/repos/daemonkit
```
Replace output_dir with the desired path for daemon outputs.


## Daemon Examples
### hello_world.py
This example creates a daemon that prints "Hello, World!" to hello_world_output.txt and records the process ID in hello_world_pid.txt. To run the example:
```
python3 examples/hello_world.py
```
### data_processer.py
The data_processor.py example reads data from raw_data.txt, processes each word, and saves the output to processed_data.txt. To run the example:
```
python3 examples/data_processer.py
```

## Daemon Template
You can create your own daemon processes using daemon_template.py. Include the tasks you want to run in the user_task() function:
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

Example with No Daemons Running:
```
% python3 manage_daemon.py                                  
No daemons are currently running.
```

Example with a Running Daemon:
```
% python3 manage_daemon.py                
1) daemon_template
Select a daemon to stop (or 0 to stop all): 1
Stopped daemon 'daemon_template' with PID 63821.
```

## Slaying the daemon
If needed, you can manually terminate a daemon by obtaining the Process ID (PID) from the corresponding PID file located in the pids directory.
### UI
Open the Activity Monitor app and look for a Python or Python3 process with the same PID as the daemon. Terminate the process by clicking on it and then clicking the 'X'.
### CLI
Terminate the daemon using:
```
kill <daemon pid>
```
Replace <daemon_pid> with the actual PID of the daemon.