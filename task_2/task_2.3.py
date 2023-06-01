from pyspark import SparkContext
import time

sc = SparkContext("local", "Prime Factor Count")

def count_prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return len(factors)


numbers = []
start = time.time()
with open('numbers.bin', 'r') as f:
    for line in f:
        numbers.append(int(line.strip()))
    f.close()
numbers = sc.parallelize(numbers)
prime_factor_counts = numbers.map(count_prime_factors)
total_prime_factor_count = prime_factor_counts.reduce(lambda x, y: x + y)
end = time.time()
print("Total prime factor count:", total_prime_factor_count)
print("Time:", end-start)  #Time: 3.4794154167175293 sec

sc.stop() 