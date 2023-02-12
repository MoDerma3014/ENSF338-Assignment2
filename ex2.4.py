import cProfile as cp
import sys
import json
import urllib.request as ulb
import timeit
import matplotlib.pyplot as plt
import numpy as np
import random
sys.setrecursionlimit(200000)

    # old functions 
"""
def func1(arr, low, high):
 if low < high:
    pi = func2(arr, low, high)
    # pi = random.randint(low,high)
    func1(arr, low, pi-1)
    func1(arr, pi + 1, high)

def func2(array, start, end):
    # index = random.randint(start,end)
    # p = array[index] # case 1, p = start; case 2, start < p < end, case 3 p = end
    p = array[start]
    low = start
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high
"""

    # new functions
def split(arr, start, end, pivot):
    """ This function splits the workload
    of the quicksort into multiple subarrays 
    to apply the method of divide and conquer
    for the function partition
    
    parameters:
    arr -- The array is going to come in already sorted pivot wise
    start -- index of first element
    end -- index of last element
    pivot -- carrying over the pivot from quicksort 
        to know where to split it from
    
    returns: -- either splitting the array in two or 
    performing one quicksort on """

    if start < end: # garantees that the size of the arr is > 1
        # determine the splitting
        
        if (start < pivot < end): # splits if pivot is between start and end
            # split
            personal_quicksort(arr, start, pivot - 1)
            personal_quicksort(arr, pivot + 1, end)
        
        # no splits if pivot is either start or end
        elif pivot == start: 
            personal_quicksort(arr,pivot + 1,end)
        elif pivot == end:
            personal_quicksort(arr, start, pivot - 1)
        

def personal_quicksort(arr, start, end):
    """Call this function first for quicksorting
    an array. Find pivot with a random index from
    start to end, doing this to not always choose 
    the start as the pivot while giving more chance
    to choose the true middle point to apply 
    divide and conquer more.
    
    Parameters:
    arr -- this is the array
    start -- index of the first element of the arr
    end -- index of the last element of the arr"""

    if start >= end: # checks if its sorting only one element in the array
        return
    
    pivot = random.randint(start,end)
    p = arr[pivot]
    low = start
    high = end
   
    # low 
    while True:
        # cycling through low
        while (arr[low] <= p and low <= high and low != pivot):
            low += 1
        # cycling through high
        while (arr[high] >= p and low <= high and high != pivot):
            high -= 1
        if (high <= low):
            break
        else:
            # changing the values
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp
            # moving pivot when it gets moved
            if (low == pivot):
                pivot = high
                
            elif (high == pivot):
                pivot = low
    # when its done sorting the array from pivot
    # its splits the array into smaller quicksorting
    split(arr, start, end, pivot)


def check_sort(arr):
    """Checks if the array is sorted or not by returning string
    and the location of not sorted status
    """

    for index,list_i in enumerate(arr):

        for current_element in range(1,len(list_i)):

            if list_i[current_element] < list_i[current_element - 1]:
                return ("Its not sorted: list: {}, index: {}".format(index,current_element))

    return "Its sorted"



def main():
    
    with open("ex2.json") as j:
        data = json.load(j)

    
    # Testing personal_quicksort
    times = []
    
    for i in data:
        lenght = len(i) - 1
        times.append(timeit.timeit(lambda:personal_quicksort(i,0,lenght), number=1))
    
    
    # Calculating time taken for program to run
    # cumulatively
    temp = 0
    cumulative_times = []
    
    for i in times:
        temp += i
        cumulative_times.append(temp)
    
    # Setting up initial values
    number_of_lists = len(data)
    x_ticks = [x for x in range(0,number_of_lists)] 

    # Time cumulative graph
    plt.figure(figsize=(10,8))
    plt.subplot(1,2,2)
    plt.plot(cumulative_times, label="Time cumulative", color="blue")
    plt.xticks(x_ticks)
    plt.xlabel("Index")
    plt.ylabel("Time in seconds")
    plt.title("Cumulative time of running\npersonal_quicksort on all lists")
    plt.legend()

    # Time graph
    plt.subplot(1,2,1)
    plt.plot(times, label = "Times of lists", color="red")
    plt.xticks(x_ticks)
    plt.title("Time taken for personal_quicksort\n to sort in function of list indices")
    plt.xlabel("Index")
    plt.ylabel("Time in seconds")
    plt.legend()

    # Logging 
    print(times)
    print(cumulative_times)

    # Checks if its sorted
    print(check_sort(data))

    # Writes data to a file to check
    """
    json_object = json.dumps(data)
    with open("ex2_result.json", "w") as j:
        j.write(json_object)
    """
    # To show in graph that its sorted
    extra_text_fig = "Status of lists: {}".format(check_sort(data))
    plt.figtext(.4, .95, extra_text_fig)
    plt.show()

    return 0

if __name__ == '__main__':
    main()
