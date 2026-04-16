import time
import os
from sort import Sort
class bsort(Sort):
    def __init__(self):
        self.time_taken = 0
        return

    def sort(self, arr):
        start = time.time()
        for j in range(len(arr)):
            for i in range(len(arr) - 1):
                if arr[i + 1] < arr[i]:
                    temp = arr[i + 1]
                    arr[i + 1] = arr[i]
                    arr[i] = temp
        end = time.time()
        self.time_taken = end - start
        self.print(arr, self.time_taken, "O(n^2)")