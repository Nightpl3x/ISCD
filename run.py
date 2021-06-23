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
    """Restart class Error to prevent the script from using to much memory after first run"""

# =============================================================================
# main
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
            raise Restart("Restarting script to save memory ...")
        
        # =============================================================================
        # handle exceptions and completly restart script
        # =============================================================================
        except IndexError:
            print("\nSorry but there are no pictures in here...\nTrying again in 30s ...")
            time.sleep(30)
            os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run 

        except Restart:
            print("\nRestarting in 15s ...")
            time.sleep(15)
            os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run               

        except KeyboardInterrupt:
            print("\nTask stopped by user...")

        else:
            print("Something happend....")
            break


