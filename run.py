# ==========================================================================================================================================================#
#                                                   run.py - file for running script and handle exceptions
# ==========================================================================================================================================================#

# =============================================================================
# Imports
# =============================================================================
import os
import sys
import time

from platform import system

# =============================================================================
# Create error class to force restart
# =============================================================================
class Restart(LookupError):
    """Restart Error to prevent the script from using to much memory after every Phase and cycle runthrough"""

def restart():
        print("---------------------------------------------")
        print("\nContiniung in 10s ...")
        print("---------------------------------------------")
        time.sleep(10)

        # restart program with exact the same command line arguments as it was originally run
        # this step is absolutely needed as otherwise the CPU and RAM usage of each Phase and Cycle stack up
        os.execv(sys.executable, ['python'] + sys.argv) 

# =============================================================================
# Script may be stopped pressing 'Ctrl+C' two times
# =============================================================================  
def master():

    if system() == "Windows":     

        try:
            import memory_profiler
            # =======================================================================================           
            # get time and memory usage pre running (not supported on raspberry pi)
            # =======================================================================================           
            m1 = memory_profiler.memory_usage()
            t1 = time.process_time()
            # =======================================================================================           
            # run main
            # ======================================================================================= 
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
            restart()

    if system() == "Linux":  

        try:

            import main
            main.cycle()
            raise Restart
        
        except Restart:
            restart()
              
    else:
        print("Sorry but this script is only designed to work on Windows or Linux")


if __name__ == '__main__':
    master()
    pass

