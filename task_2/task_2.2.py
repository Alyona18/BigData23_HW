from multiprocessing import Pool, cpu_count
import time


def count_prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors


def worker(n: int) -> int:
    return len(count_prime_factors(n))

def parallel_count() -> int:
    with open('numbers.bin', "r") as f:
        numbers = [int(line.strip()) for line in f]

    with Pool(cpu_count()) as p:
        result = p.map(worker, numbers)

    return sum(result)

if __name__ == '__main__':
    
    start = time.time()
    total_factors = parallel_count()
    end = time.time()
    print("Result: ", total_factors)
    print("Time: ", end-start) # 2.5098180770874023 sec


