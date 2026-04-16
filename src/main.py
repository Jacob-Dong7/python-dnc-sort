from mergesort import msort
from bubblesort import bsort
from quicksort import quicksort
from selectionsort import selection_sort
import time
def main():
    bubble_sort = bsort()
    merge_sort = msort()
    quick_sort = quicksort()
    select_sort = selection_sort()
    while True:
        menu()

        user_input = input("Select Option ")

        if user_input == "-1":
            print("Quitting...")
            quit()
        #Bubble Sort
        elif user_input == "1":

            arr = bubble_sort.start()
            if arr == -1:
                 continue
            bubble_sort.sort(arr)
        #Selection Sort
        elif user_input == "2":
            arr = select_sort.start()
            if arr == "-1":
                continue
            select_sort.sort(arr)


        #Quick Sort
        elif user_input == "5":

            arr = quick_sort.start()
            if arr == -1:
                continue
            quick_sort.sort(arr)
        
        #Merge Sort
        elif user_input == "4":

            arr = merge_sort.start()
            if arr == -1:
                continue
            start = time.time()
            result = merge_sort.sort(arr)
            end = time.time()
            merge_sort.print(result, end - start, "O(log(n))")

    return

def array_check(arr):
    if arr == "-1":
        return False
    else:
        return True
    
def menu():
    print("\n" + "="*40)
    print("        SORTING MENU")
    print("="*40)
    print("[1] Bubble Sort")
    print("[2] Selection Sort")
    print("[3] Insertion Sort")
    print("[4] Merge Sort")
    print("[5] Quick Sort")
    print("[6] Binary Search")
    print("[7] Quick Select")
    print("[-1] Exit")
    print("="*40)

if __name__ == "__main__":
    main()