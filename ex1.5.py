import matplotlib.pyplot as plt
import timeit

def func(n):
    if (n == 0) or (n == 1):
        return n
    else:
        return func(n-1) + func(n-2)

elapsed_time = timeit.timeit(lambda: func(35),number=1)
print(f'Elapsed time for the original code: {elapsed_time} seconds')

def fib2(n, cache={}):
    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib2(n-1) + fib2(n-2)
            return cache[n]
elapsed_time = timeit.timeit(lambda: fib2(35),number=1)
print(f'Elapsed time for the optimized code: {elapsed_time} seconds')

original_times = []
improved_times = []

for i in range(36):
    original_time = timeit.timeit(lambda: func(i), number=1)
    original_times.append(original_time)
    improved_time = timeit.timeit(lambda: fib2(i), number=1)
    improved_times.append(improved_time)

plt.plot(original_times, label='Original')
plt.plot(improved_times, label='Improved')
plt.xlabel('Input size (n)')
plt.ylabel('Execution time (seconds)')
plt.legend()
plt.show()




