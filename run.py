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

import main

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
        # handle exceptions and completly restart script (t-10s on time.sleep() as we already have 10s inside the main.py)
        # ===================================================================================================================
        except IndexError:
            print("---------------------------------------------")
            print("\nSorry but there are no pictures in here...\nTrying again in 60s ...")
            print("---------------------------------------------")
            time.sleep(50)
            os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run 

        except Restart:
            print("---------------------------------------------")
            print("\nRestarting in 15s ...")
            print("---------------------------------------------")
            time.sleep(5)
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


