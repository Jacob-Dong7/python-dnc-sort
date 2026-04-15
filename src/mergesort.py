class msort:
    def __init__(self):
        return
    
    def sort(self, arr):
        n = len(arr)
        if n <= 1:
            return arr
        
        mid = int(len(arr)) / 2
        
        left = arr[0:int(mid)]
        right = arr[int(mid):n]

        left = self.sort(left)
        right =  self.sort(right)

        result = self.merge(left, right, arr)
        return result
    
    def merge(self, left, right, main):
        i = 0
        j = 0
        k = 0
        p = len(left)
        q = len(right)

        while i < p and j < q:
            if left[i] <= right[j]:
                main[k] = left[i]
                i += 1
            else:
                main[k] = right[j]
                j += 1
            k += 1

        if i == p:
            while j < q:
                main[k] = right[j]
                j += 1
                k += 1
        else:
            while i < p:
                main[k] = left[i]
                i += 1
                k += 1         
        return main
    
    def print(self, arr):
        for element in arr:
            print(element,end=" ")