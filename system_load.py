
import os
import cv2
import glob
import time
import memory_profiler

import utils as xct
import main as mc
import MRCNN_Balloon as mrb


def YieldGenerator():
            
        if __name__ == '__main__':
            m1 = memory_profiler.memory_usage()
            t1 = time.process_time()

            #cubes = check_even_new(range(1000000))
            cubes = mc.test()
            #cubes = mrb.MRCNN_Balloon(IMAGE_DIRECTORY_CAM, images_cam)

            t2 = time.process_time()
            m2 = memory_profiler.memory_usage()
            time_diff = t2 - t1
            mem_diff = m2[0] - m1[0]
            print(f"\nIt took {time_diff} Secs and {mem_diff} Mb to execute this method")
