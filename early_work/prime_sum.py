import math
import time

start_time = time.perf_counter()

sum_of_primes = 0
for n in range(2, 100000):
    is_prime = True
    if n % 2 == 0 and n > 2:
        is_prime = False
    else:
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                is_prime = False
                break
    if is_prime:
        sum_of_primes += n

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time:.6f} seconds")
print(f"{sum_of_primes:,}")