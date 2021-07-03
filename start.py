import subprocess as subp
from platform import system

if system() == "Windows": 

    print("Windows OS")

    python_bin = "env/Scripts/python" # Path to a Python interpreter inside the virtualenv
    script_file = "user_interface.py" # Path to the script that must run under the virtualenv
    subp.Popen([python_bin, script_file])   

elif system() == "Linux":    

    print("Linux OS")

    python_bin = "env/bin/python" # Path to a Python interpreter inside the virtualenv
    script_file = "user_interface.py" # Path to the script that must run under the virtualenv
    subp.Popen([python_bin, script_file]) 

else:
    print("Sorry but this script is only designed to work on Windows or Linux")