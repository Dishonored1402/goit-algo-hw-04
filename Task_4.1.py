import timeit
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def timsort(arr):
    arr.sort()

def measure_time(sort_function, arr):
    return timeit.timeit(lambda: sort_function(arr.copy()), number=10)

sizes = [100, 1000, 5000, 10000]
results = []

for size in sizes:
    random_data = [random.randint(0, 10000) for _ in range(size)]
    
    merge_time = measure_time(merge_sort, random_data)
    insertion_time = measure_time(insertion_sort, random_data)
    timsort_time = measure_time(timsort, random_data)
    
    results.append((size, merge_time, insertion_time, timsort_time))

for result in results:
    print(f"Size: {result[0]}")
    print(f"Merge Sort Time: {result[1]:.6f} seconds")
    print(f"Insertion Sort Time: {result[2]:.6f} seconds")
    print(f"Timsort Time: {result[3]:.6f} seconds")
    print("-" * 30)
