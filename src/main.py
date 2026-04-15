from mergesort import msort
import time
def main():
    merge_sort = msort()
    arr = [38, 27, 43, 3, 9, 82, 10, 55, 21, 7, 60, 14, 1, 99, 35, 18, 72, 6, 49, 25]
    start = time.time()
    result = merge_sort.sort(arr)
    end = time.time()
    print(f"Time taken = {end - start:.5f} seconds")
    merge_sort.print(result)
    return

if __name__ == "__main__":
    main()