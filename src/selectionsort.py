from sort import Sort
class selection_sort(Sort):
    def __init__(self):
        return
    
    def sort(self, array):
        n = len(array)
        for i in range(n):
            min = array[i]
            index = i
            for j in range(i + 1, n):
                if array[j] < min:
                    min = array[j]
                    index = j
            array[i], array[index] = array[index], array[i]


        return