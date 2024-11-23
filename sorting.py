import random
import time

x = [random.randint(1, 100) for _ in range(100)]

def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    return array

start_bubble = time.time()
bubble_sorted = bubble_sort(x[:])
end_bubble = time.time()

start_merge = time.time()
merge_sorted = merge_sort(x[:])
end_merge = time.time()

print("Array Awal:", x)
print("Array Bubble Sort:", bubble_sorted)
print("Array Merge Sort:", merge_sorted)
print("Waktu komputasi Bubble Sort:", end_bubble - start_bubble, "seconds")
print("Waktu komputasi Merge Sort:", end_merge - start_merge, "seconds")


# Pseudocode bubblesort
# ...
# BUBBLE_SORT(array):
#     n = length(array)
#     for i from 0 to n-1:
#         for j from 0 to n-i-2:
#             if array[j] > array[j+1]:
#                 swap(array[j], array[j+1])
# Analisis:
# Big-O : O(n^2)
# Big-Theta: O(n)



# Pseudocode mergesort
# ...
# MERGE_SORT(array):
#     if length(array) > 1:
#         mid = length(array) // 2
#         left = array[0:mid]
#         right = array[mid:]
        
#         MERGE_SORT(left)
#         MERGE_SORT(right)
        
#         i = j = k = 0
#         while i < length(left) and j < length(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i = i + 1
#             else:
#                 array[k] = right[j]
#                 j = j + 1
#             k = k + 1
        
#         while i < length(left):
#             array[k] = left[i]
#             i = i + 1
#             k = k + 1
        
#         while j < length(right):
#             array[k] = right[j]
#             j = j + 1
#             k = k + 1
# analisis:
# Big-O: O(n log n)
# Big-Theta: O(n log n)