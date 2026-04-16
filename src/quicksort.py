from sort import Sort
import time
class quicksort(Sort):
    def __init__(self):
        return
    
    def sort(self, array):
        start = time.time()
        self.quick_sort(array, 0, len(array) - 1)
        end = time.time()
        self.print(array, end - start, "nlog(n)")



    def quick_sort(self, array, l, r):
        if l < r:
            pivot = self.partition(array, l, r)
            self.quick_sort(array, l, pivot - 1)
            self.quick_sort(array, pivot + 1, r)

    def partition(self, array, l, r):
        pivot = array[l]
        left = l
        right = r + 1

        while True:
            left += 1
            while array[left] < pivot and left < r:
                left += 1
            right -= 1
            while array[right] > pivot:
                right -= 1
            if left >= right:
                break
            array[left], array[right] = array[right], array[left]
        array[l], array[right] = array[right], array[l]
        return right
    
"""2 1 3"""