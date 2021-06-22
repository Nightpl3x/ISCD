import time
import memory_profiler

import main

            
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
            print("\nRestarting in 10s ...")
            time.sleep(10)

        except KeyboardInterrupt:
        
            print("Task stopped by user...")
            raise

