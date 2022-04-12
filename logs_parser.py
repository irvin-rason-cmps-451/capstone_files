import re
import os
import time
import psutil

import cv2
import pytesseract
from memory_profiler import profile

@profile
def control():
    '''
    Traverse through the Kubernetes logs .txt file varient and return the price

    Note:
        - Time to Complete
        - Memory Usage
        - CPU Usage

    Time Complexity: O(2n)
    '''
    initial_cpu = psutil.cpu_percent()
    start = time.time()

    with open("/Users/rasonirvin/Desktop/Irvin, Rason CMPS 451 Source Code/capstone_files/sample_kube_logs.txt", "r") as f:
        lines = f.read().splitlines()
        f.close()

    count = 0
    for line in lines:
        if 'ERROR' in line:
            count+=1
            # track data
            end = time.time()
            print(f'Time to complete: {end-start}')
            print(f'CPU Usage: {psutil.cpu_percent(end-start)}')

    return count


@profile
def hypothesized():
    '''
    Traverse through the Kubernetes logs .jpeg file varient and return the price

    Note:
        - Time to Complete
        - Memory Usage
        - CPU Usage

    Time Complexity: O(1)
    '''
    initial_cpu = psutil.cpu_percent()
    start = time.time()
    
    img = cv2.imread("/Users/rasonirvin/Desktop/Irvin, Rason CMPS 451 Source Code/capstone_files/sample_kube_logs.jpeg")
    # crop image to focus area
    roi = img[0:994, 425:558]
    # track data
    end = time.time()
    print('Time to complete: {}'.format(end-start))
    print('CPU Usage: {}'.format(psutil.cpu_percent(end-start)))

    return pytesseract.image_to_string(roi).count("ERROR")


def main():
    '''
    Run the control and hypothesized groups 10 times to get a baseline for data analysis

    Note:
        - File Size
    '''
    # control run
    txt_size = os.path.getsize('/Users/rasonirvin/Desktop/Irvin, Rason CMPS 451 Source Code/capstone_files/sample_kube_logs.txt')
    print(f'.txt File Size: {txt_size}')
    for i in range(10):
        print(control())

    # hypothesized run
    jpeg_size = os.path.getsize("/Users/rasonirvin/Desktop/Irvin, Rason CMPS 451 Source Code/capstone_files/sample_kube_logs.jpeg")
    print(f'.jpeg File Size: {jpeg_size}')
    for i in range(10):
        hypothesized()

        
if __name__ == "__main__":
    main()