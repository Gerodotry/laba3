import time
import sympy as sp
import matplotlib.pyplot as plt
from multiprocessing.pool import ThreadPool
import scipy.integrate as spi

x = sp.Symbol('x')
f = sp.sin(x) + sp.exp(x)  # Функція, для якої обчислюємо невизначений інтеграл

def compute_integral_sequential(x_values):
    results = []
    for x_value in x_values:
        integral = sp.integrate(f, x).subs(x, x_value)
        results.append(integral)
    return results

def compute_integral_parallel(x_value):
    integral = sp.integrate(f, x).subs(x, x_value)
    return integral

def compute_integral_definite(a, b):
    result, error = spi.quad(lambda x: sp.sin(x) + sp.exp(x), a, b)
    return result

x_values = [1, 2, 3, 4, 5]  # Значення x, для яких обчислюємо невизначений інтеграл
intervals = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]  # Інтервали для обчислення визначеного інтегралу

# Виміряємо час виконання для послідовної версії невизначеного інтегралу
start_time = time.time()
results_sequential = compute_integral_sequential(x_values)
end_time = time.time()
execution_time_sequential = end_time - start_time

print("Невизначені інтеграли (послідовна версія): ", results_sequential)
print("Час виконання (послідовна версія): ", execution_time_sequential, "секунд")

# Виміряємо час виконання для паралельної версії невизначеного інтегралу
pool = ThreadPool()
start_time = time.time()
results_parallel = pool.map(compute_integral_parallel, x_values)
end_time = time.time()
execution_time_parallel = end_time - start_time

print("Невизначені інтеграли (паралельна версія): ", results_parallel)
print("Час виконання (паралельна версія): ", execution_time_parallel, "секунд")

# Виміряємо час виконання для послідовної версії визначеного інтегралу
start_time = time.time()
results_sequential_definite = [compute_integral_definite(a, b) for a, b in intervals]
end_time = time.time()
execution_time_sequential_definite = end_time - start_time

print("Визначені інтеграли (послідовна версія): ", results_sequential_definite)
print("Час виконання (послідовна версія): ", execution_time_sequential_definite, "секунд")

# Виміряємо час виконання для паралельної версії визначеного інтегралу
pool = ThreadPool()
start_time = time.time()
results_parallel_definite = pool.starmap(compute_integral_definite, intervals)
end_time = time.time()
execution_time_parallel_definite = end_time - start_time

print("Визначені інтеграли (паралельна версія): ", results_parallel_definite)
print("Час виконання (паралельна версія): ", execution_time_parallel_definite, "секунд")
# Виміряємо час виконання для послідовної версії невизначеного інтегралу
sequential_execution_times = []
for _ in range(10):
    start_time = time.time()
    results_sequential = compute_integral_sequential(x_values)
    end_time = time.time()
    execution_time_sequential = end_time - start_time
    sequential_execution_times.append(execution_time_sequential)

# Виміряємо час виконання для паралельної версії невизначеного інтегралу
parallel_execution_times = []
for _ in range(10):
    pool = ThreadPool()
    start_time = time.time()
    results_parallel = pool.map(compute_integral_parallel, x_values)
    end_time = time.time()
    execution_time_parallel = end_time - start_time
    parallel_execution_times.append(execution_time_parallel)

    #grafic
plt.plot(range(1, 11), sequential_execution_times, label='Sequential')
plt.plot(range(1, 11), parallel_execution_times, label='Parallel')
plt.xlabel('Iteration')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time Comparison')
plt.legend()
plt.show()
