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
    
    def start(self):   
        user_input = self.get_test()
        
        path = os.path.join("test", user_input)
        arr = []

        if not user_input.endswith(".txt"):
            print("File Must End With .txt")
            return -1
        elif not os.path.isfile(path):
            print("Invalid File")
            return -1
        
        else:
            with open(path) as f:
                for data in f:
                    arr.extend(int(x) for x in data.split())
        return arr
                 