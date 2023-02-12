import sys
import timeit
import json
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def quick_sort(arr, low, high):
    """Recursive function for sorting using quicksort algorithm"""
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)

def partition(array, start, end):
    """Helper function for finding pivot and partitioning the array"""
    pivot = array[start]
    left = start + 1
    right = end
    while True:
        while left <= right and array[right] >= pivot:
            right = right - 1
        while left <= right and array[left] <= pivot:
            left = left + 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
        else:
            break
    array[start], array[right] = array[right], array[start]
    return right

# Load the dataset
with open("ex2.json","r") as f:
    datasets = json.load(f)

time_quick = []
time_part = []
index = []

# Measure the time taken for sorting using quick_sort
for i in range(len(datasets)):
    time_quick.append(timeit.timeit(lambda: quick_sort(datasets[i],i,len(datasets[i])-1), number=1))

# Measure the time taken for sorting using partition
for i in range(len(datasets)):
    time_part.append(timeit.timeit(lambda: partition(datasets[i],i,len(datasets[i])-1), number=1))
    index.append(i)

# Plot the time taken by quick_sort and partition on a single graph
plt.plot(index, time_quick, label='quick_sort')
plt.plot(index, time_part, label='partition')
plt.xlabel("Number of times function called")
plt.ylabel("Time taken (seconds)")
plt.title("Performance Comparison of quick_sort and partition")
plt.legend()
plt.show()