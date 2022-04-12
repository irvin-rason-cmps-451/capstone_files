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
    Traverse through the advertisement .txt file varient and return the price

    Note:
        - Time to Complete
        - Memory Usage
        - CPU Usage

    Time Complexity: O(2n)
    '''
    initial_cpu = psutil.cpu_percent()
    start = time.time()

    with open("/Users/rasonirvin/Desktop/Irvin, Rason CMPS 451 Source Code/sample_advertisement.txt", "r") as f:
        lines = f.read().splitlines()
        f.close()

    price = 0
    for line in lines:
        price = re.findall('\$(\d{1,3})', line)

        if len(price) > 0:
            end = time.time()
            # track data
            print(f'Time to complete: {end-start}')
            print(f'CPU Usage: {psutil.cpu_percent(end-start)}')
            return '$' + price[0]
    
    return None


@profile
def hypothesized():
    '''
    Traverse through the advertisement .jpeg file varient and return the price

    Note:
        - Time to Complete
        - Memory Usage
        - CPU Usage

    Time Complexity: O()
    '''
    initial_cpu = psutil.cpu_percent()
    start = time.time()

    img = cv2.imread("/Users/rasonirvin/Desktop/Irvin, Rason CMPS 451 Source Code/sample_advertisement.jpeg")
    # crop image to focus area
    roi = img[50:220, 372:500]
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
    txt_size = os.path.getsize('/Users/rasonirvin/Desktop/Irvin, Rason CMPS 451 Source Code/sample_advertisement.txt')
    print(f'.txt File Size: {txt_size}')
    for i in range(10):
        print(control())

    # hypothesized run
    jpeg_size = os.path.getsize("/Users/rasonirvin/Desktop/Irvin, Rason CMPS 451 Source Code/sample_advertisement.jpeg")
    print(f'.jpeg File Size: {jpeg_size}')
    for i in range(10):
        hypothesized()


if __name__ == "__main__":
    main()