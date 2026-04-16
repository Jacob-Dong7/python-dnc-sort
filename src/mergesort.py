from sort import Sort
class msort(Sort):

    def __init__(self):
        self.time_taken = 0
        return
    
    def sort(self, arr):
        return
    
    def print(self, arr):
        print("="*40)
        print("        MERGE SORT RESULT")
        for item in arr:
            print(item,end=" ")
        print("="*40)
        print(f"Time Taken = {self.time_taken} seconds\n")
        print("Complexity = O(log(n))")
