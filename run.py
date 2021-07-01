# ==========================================================================================================================================================#
#                                                   run.py - file for running script and handle exceptions
# ==========================================================================================================================================================#

# =============================================================================
# Imports
# =============================================================================
import os
import sys
import time
import memory_profiler

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
def master():

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
        cubes = main.cycle()
        # =======================================================================================           
        # get time and memory usage after running (comment out when running on raspberry pi)
        # =======================================================================================                      
        t2 = time.process_time()
        m2 = memory_profiler.memory_usage()
        time_diff = t2 - t1
        mem_diff = m2[0] - m1[0]
        print(f"\nIt took {time_diff} Secs and {mem_diff} Mb to execute this method")
        # =======================================================================================           
        # raise error class to restart
        # =======================================================================================           
        raise Restart
    
    # ===================================================================================================================
    # handle exceptions and restart script loop
    # ===================================================================================================================

    except Restart:
        print("---------------------------------------------")
        print("\nContiniung in 15s ...")
        print("---------------------------------------------")
        time.sleep(15)

        # restart program with exact the same command line arguments as it was originally run
        # this step is absolutely needed as otherwise the CPU and RAM usage of each Phase and Cycle stack up
        os.execv(sys.executable, ['python'] + sys.argv) 

    else:
        print("---------------------------------------------")
        print("Something happend....")
        print("---------------------------------------------")
        sys.exit()


if __name__ == '__main__':
    master()
    pass

