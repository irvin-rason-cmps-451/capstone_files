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
    Traverse through the resume .txt file varient and return the price

    Note:
        - Time to Complete
        - Memory Usage
        - CPU Usage

    Time Complexity: O(2n)
    '''
    initial_cpu = psutil.cpu_percent()
    start = time.time()

    with open("/Users/rasonirvin/Desktop/Irvin, Rason CMPS 451 Source Code/capstone_files/sample_resume.txt", "r") as f:
        lines = f.read().splitlines()
        f.close()

    for i in range(len(lines)):
        if 'Skills:' in lines[i]:
            return lines[i].split(': ')[1] + ' ' + lines[i+1]

            # track data
            end = time.time()
            print('Time to complete: {}'.format(end-start))
            print('CPU Usage: {}'.format(psutil.cpu_percent(end-start)))

    return 'No skills present :('


@profile
def hypothesized():
    '''
    Traverse through the resume .jpeg file varient and return the price

    Note:
        - Time to Complete
        - Memory Usage
        - CPU Usage

    Time Complexity: O(1)
    '''
    initial_cpu = psutil.cpu_percent()
    start = time.time()

    img = cv2.imread("/Users/rasonirvin/Desktop/Irvin, Rason CMPS 451 Source Code/capstone_files/sample_resume.jpeg")
    # crop image to focus area
    roi = img[648:671, 25:525]
    # track data
    end = time.time()
    print('Time to complete: {}'.format(end-start))
    print('CPU Usage: {}'.format(psutil.cpu_percent(end-start)))

    return pytesseract.image_to_string(roi)


def main():
    '''
    Run the control and hypothesized groups 10 times to get a baseline for data analysis

    Note:
        - File Size
    '''
    # control run
    txt_size = os.path.getsize('/Users/rasonirvin/Desktop/Irvin, Rason CMPS 451 Source Code/capstone_files/sample_resume.txt')
    print(f'.txt File Size: {txt_size}')
    for i in range(10):
        print(control())

    # hypothesized run
    jpeg_size = os.path.getsize("/Users/rasonirvin/Desktop/Irvin, Rason CMPS 451 Source Code/capstone_files/sample_resume.jpeg")
    print(f'.jpeg File Size: {jpeg_size}')
    for i in range(10):
        print(hypothesized())



if __name__ == "__main__":
    main()
            
    