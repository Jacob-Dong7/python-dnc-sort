from sort import Sort
import time
class msort(Sort):

    def __init__(self):
        self.time_taken = 0
        return
    
    def sort(self, arr):
        length = len(arr)
        mid = length / 2

        if length <= 1:
            return arr
        
        left = arr[0:int(mid)]
        right = arr[int(mid):length]

        left = self.sort(left)
        right = self.sort(right)
        result = self.merge(left, right, arr)

        return result
    
    def merge(self, left, right, arr):
        curr_left = 0
        curr_right = 0

        max_left = len(left)
        max_right = len(right)

        curr = 0

        while curr_left < max_left and curr_right < max_right:
            if left[curr_left] <= right[curr_right]:
                arr[curr] = left[curr_left]
                curr_left += 1
            else:
                arr[curr] = right[curr_right]
                curr_right += 1
            curr += 1
        if curr_left == max_left:
            while curr_right < max_right:
                arr[curr] = right[curr_right]
                curr_right += 1
                curr += 1
        else:
            while curr_left < max_left:
                arr[curr] = left[curr_left]
                curr_left += 1
                curr += 1
        return arr

