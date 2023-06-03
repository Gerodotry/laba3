import sympy as sp
import time
from multiprocessing.pool import ThreadPool
import scipy.integrate as spi


# Послідовна версія обчислення невизначеного інтегралу
def compute_integral_sequential(x_values):
    start_time = time.time()

    integrals = []
    for x_value in x_values:
        integral = sp.integrate(f, x).subs(x, x_value)
        integrals.append(integral)

    end_time = time.time()
    execution_time = end_time - start_time

    print("Послідовна версія: ", integrals)
    print("Час виконання: ", execution_time)


# Паралельна версія обчислення невизначеного інтегралу
def compute_integral_parallel(x_values):
    start_time = time.time()

    def compute_integral(x_value):
        integral = sp.integrate(f, x).subs(x, x_value)
        return integral

    pool = ThreadPool()
    integrals = pool.map(compute_integral, x_values)

    end_time = time.time()
    execution_time = end_time - start_time

    print("Паралельна версія: ", integrals)
    print("Час виконання: ", execution_time)


# Послідовна версія обчислення визначеного інтегралу
def compute_integral_definite_sequential(intervals):
    start_time = time.time()

    integrals = []
    for a, b in intervals:
        result, error = spi.quad(f, a, b)
        integrals.append(result)

    end_time = time.time()
    execution_time = end_time - start_time

    print("Послідовна версія: ", integrals)
    print("Час виконання: ", execution_time)


# Паралельна версія обчислення визначеного інтегралу
def compute_integral_definite_parallel(intervals):
    start_time = time.time()

    def compute_integral(a, b):
        result, error = spi.quad(f, a, b)
        return result

    pool = ThreadPool()
    integrals = pool.starmap(compute_integral, intervals)

    end_time = time.time()
    execution_time = end_time - start_time

    print("Паралельна версія: ", integrals)
    print("Час виконання: ", execution_time)


# Вхідні дані
x_values = [1, 2, 3, 4, 5]
intervals = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

# Обчислення невизначеного інтегралу
compute_integral_sequential(x_values)
compute_integral_parallel(x_values)

# Обчислення визначеного інтегралу
compute_integral_definite_sequential(intervals)
compute_integral_definite_parallel(intervals)
