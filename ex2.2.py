import cProfile as cp
import sys
import json
import urllib.request as ulb
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):
 if low < high:
    pi = func2(arr, low, high)
    func1(arr, low, pi-1)
    func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
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


def main():
    
    with open("ex2.json") as j:
        data = json.load(j)
    
    times = []
    
    # cycling to different lists in data
    for i in data:
        lenght = len(i) - 1
        times.append(timeit.timeit(lambda:func1(i,0, lenght), number=1))
    
    temp = 0
    cumulative_times = []
    
    for i in times:
        temp += i
        cumulative_times.append(temp)
    
    # Time cumulative graph
    plt.subplot(1,2,2)
    plt.plot(cumulative_times, label="Time cumulative", color="blue")
    plt.xlabel("Index")
    plt.ylabel("Time in seconds")
    plt.title("Cumulative time of running\nfunc1 on all lists")
    plt.legend()

    # Time graph
    number_of_lists = len(data)
    plt.subplot(1,2,1)
    plt.plot(times, label = "times of lists", color="red")
    plt.title("Time taken for {} lists to\nrun of a function of list indices".format(number_of_lists))
    plt.xlabel("Index")
    plt.ylabel("Time in seconds")
    plt.legend()


    plt.show()

    return 0

if __name__ == '__main__':
    main()
