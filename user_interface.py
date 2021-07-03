import os
import sys
import signal
import tkinter as tk
import subprocess as subp

from platform import system

from directoryHandling import resetRuntimeTxt 

# =============================================================================
# Class
# =============================================================================
class Interface(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self) 

# =============================================================================
# Class-Functions
# =============================================================================
        def stop():

            with open("runtime.txt") as f:
                lines = f.readlines()
                lines[1] = "Stop: True\n"
            with open("runtime.txt", "w") as f:
                f.writelines(lines)   
            '''
            pid = os.getpid()

            from run import master
            pid_run = master

            from main import cycle
            pid_main = cycle

            if system() == "Windows":

                subp.Popen('taskkill /F /PID {0}'.format(pid))
                subp.Popen('taskkill /F /PID {0}'.format(pid_run))
                subp.Popen('taskkill /F /PID {0}'.format(pid_main))


            elif system() == "Linux":
                os.kill(pid, signal.SIGKILL)
                os.kill(pid_run, signal.SIGKILL)
                os.kill(pid_main, signal.SIGKILL)
            
            else:
                print("Task only executable on Windows and Linux")
            '''

        def help_txt():
            if system() == "Windows":
                os.system('README.md')
            else:
                try:
                    subp.call([os.environ["EDITOR"], "README.md"])
                except:
                    try:
                        subp.call(["gedit", "README.md"])
                    except:
                        subp.call(["nano", "README.md"])

# =============================================================================
# GUI Header
# =============================================================================

        self.geometry('250x400')
        self.title('ColiChecker')
        self['background']='#50A6C2'
        

        first_label = tk.Label(self, text = "\n ColiChecker GUI \n", font='Helvetica 14 bold', relief = "groove")
        first_label.pack(pady = 5, padx = 5)
# =============================================================================
# GUI Buttons
# =============================================================================
        y, x = 10, 15

        a = tk.Button(self, text="  Start \n[Continue]", command=lambda: subp.call([sys.executable, "run.py"]), activeforeground="black", activebackground="cyan", pady = y, padx = 10)
        a.pack(pady=5, padx=5)

        b = tk.Button(self, text="  Stop  ", command=stop, activeforeground="black", activebackground="orange", pady = y, padx = x)
        b.pack(pady=5, padx=5)

        c = tk.Button(self, text="  Reset ", command=resetRuntimeTxt, activeforeground="black", activebackground="cyan", pady = y, padx = x)
        c.pack(pady=5, padx=5)

        d = tk.Button(self, text="  Help  ", command=help_txt, activeforeground="black", activebackground="cyan", pady = y, padx = x)
        d.pack(pady=5, padx=5)

        e = tk.Button(self, text="  Setup ", command=lambda: subp.call([sys.executable, "setup.py"]), activeforeground="black", activebackground="orange", pady = y, padx = x)
        e.pack(pady=5, padx=5)


if __name__ == '__main__':
    user = Interface()
    user.mainloop()