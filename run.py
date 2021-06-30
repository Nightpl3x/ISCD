# ==========================================================================================================================================================#
#                                                   run.py - file for running script and handle exceptions
# ==========================================================================================================================================================#

# =============================================================================
# Imports
# =============================================================================
import os
import sys
import time
import memory_profiler # (comment out when running on raspberry pi)

import subprocess as subp
from platform import system

ROOT_DIR = os.path.abspath("../")

# =============================================================================
# Create error class to force restart
# =============================================================================
class Restart(LookupError):
    """Restart Error to prevent the script from using to much memory after first run"""
# =============================================================================
# Script may be stopped pressing 'Ctrl+C' two times
# =============================================================================           
if __name__ == '__main__':

    while True:

        try:
            # =======================================================================================           
            # get time and memory usage pre running (comment out when running on raspberry pi)
            # =======================================================================================           
            m1 = memory_profiler.memory_usage()
            t1 = time.process_time()
            # =======================================================================================           
            # run main
            # ======================================================================================= 
            '''
            if system() == "Windows":        
                python_bin = ROOT_DIR+"ColiChecker/"+"env/Scripts/python" # Path to a Python interpreter inside the virtualenv
                script_file = ROOT_DIR+"ColiChecker/"+"run.py" # Path to the script that must run under the virtualenv
                subp.Popen([python_bin, script_file])   

            elif system() == "Linux":    
                python_bin = ROOT_DIR+"ColiChecker/"+"env/bin/python" # Path to a Python interpreter inside the virtualenv
                script_file = ROOT_DIR+"ColiChecker/"+"run.py" # Path to the script that must run under the virtualenv
                subp.Popen([python_bin, script_file]) 
                
            else:
                print("Sorry but this script is only designed to work on Windows or Linux")
            '''
            import main
            cubes = main.run()
            # =======================================================================================           
            # get time and memory usage after running (comment out when running on raspberry pi)
            # =======================================================================================                      
            t2 = time.process_time()
            m2 = memory_profiler.memory_usage()
            time_diff = t2 - t1
            mem_diff = m2[0] - m1[0]
            print(f"\nIt took {time_diff} Secs and {mem_diff} Mb to execute this method")
            # =======================================================================================           
            # raise error class to force restart
            # =======================================================================================           
            raise Restart
        
        # ===================================================================================================================
        # handle exceptions and completly restart script
        # ===================================================================================================================
        except IndexError:
            print("---------------------------------------------")
            print("\nSorry but there are no pictures in here...\nTrying again in 60s ...")
            print("---------------------------------------------")
            time.sleep(60)
            os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run 

        except Restart:
            print("---------------------------------------------")
            print("\nRestarting in 15s ...")
            print("---------------------------------------------")
            time.sleep(15)
            os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run               

        except KeyboardInterrupt:
            print("---------------------------------------------")
            print("\nTask stopped by user...")
            print("---------------------------------------------")

        else:
            print("---------------------------------------------")
            print("Something happend....")
            print("---------------------------------------------")
            break


