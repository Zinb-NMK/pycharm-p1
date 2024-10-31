#How to get time of a python program's Execution

import time#time module it provides various time related functions
def timee():
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i

    end_time = time.time()
    return s , end_time - start_time
n = 5
print(timee())