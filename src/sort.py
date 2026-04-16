import os
class Sort:
    def __init__(self):
        return
    
    def print(self, arr, time_taken, complexity):
        print("="*40)
        print("        SORT RESULT")
        print("="*40)
        for i in range(len(arr)):
            if i == 0:
                print(f"[{arr[i]}, ",end="")
            elif i == len(arr) - 1:
                print(f"{arr[i]}]\n")
            else:
                print(f"{arr[i]}, ",end="")
        print("="*40)
        print(f"Time Taken = {time_taken:.5f} seconds\n")
        print(f"Complexity = {complexity}")
        print("="*40)

    def get_test(self):
        folder = "test"
        print("="*40)
        print("        TEST FILES")
        print("="*40)
        for file in os.listdir(folder):
            print(file)
        print("="*40)
        user_input = input("Select File ")
        return user_input
    
    