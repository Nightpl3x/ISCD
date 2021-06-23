import os
import sys
import time
import memory_profiler

import main

class Restart(LookupError):
    """Restart class Error to prevent the script from using to much memory after first run"""
            
if __name__ == '__main__':

    while True:

        try:
            m1 = memory_profiler.memory_usage()
            t1 = time.process_time()

            cubes = main.run()
            #cubes = mrb.MRCNN_Balloon(IMAGE_DIRECTORY_CAM, images_cam) # for testing
            #cubes = check_even_new(range(1000000)) # for testing
            
            t2 = time.process_time()
            m2 = memory_profiler.memory_usage()
            time_diff = t2 - t1
            mem_diff = m2[0] - m1[0]
            print(f"\nIt took {time_diff} Secs and {mem_diff} Mb to execute this method")
            raise Restart("Restarting script to save memory ...")

        except Restart or KeyboardInterrupt:
            
            if Restart:
                print("\nRestarting in 10s ...")
                time.sleep(10)
                os.execv(sys.executable, ['python'] + sys.argv) # restart program with exact the same command line arguments as it was originally run

            elif KeyboardInterrupt:
                print("\nTask stopped by user...")
                time.sleep(10)
            else:
                print("Something happend....")
                break
        else:
            break

