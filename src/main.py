from mergesort import msort
from bubblesort import bsort
import time
def main():
    bubble_sort = bsort()
    while True:
        menu()

        user_input = input("Select Option ")

        if user_input == "-1":
            print("Quitting...")
            quit()
        elif user_input == "1":
            arr = bubble_sort.start()
            if arr == -1:
                 continue
            bubble_sort.sort(arr)

    return

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