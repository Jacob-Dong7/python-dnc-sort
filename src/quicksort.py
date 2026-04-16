from sort import Sort
class quicksort(Sort):
    def __init__(self):
        return
    
    def sort(self, array):
        self.quick_sort(array, 0, len(array) - 1)


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
            while array[left] < pivot:
                left += 1
            right -= 1
            while array[right] > pivot:
                right -= 1
            temp = array[left]
            array[left] = array[right]
            array[right] = temp
            if left >= right:
                temp = array[right]
                array[right] = pivot
                array[l] = temp
                return right



        temp = array[left]
        array[left] = array[right]
        array[right] = temp


        return
    
    """2 5 1 3"""
    5 < 2