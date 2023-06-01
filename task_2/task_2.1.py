from random import randint
import time

def generator(fn, n):
    with open(fn, 'w') as f:
        for i in range(n):
            num = randint(0, 2**32-1)
            f.write(str(num) + '\n')

def prime_factors(n):
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

#generator('numbers.bin', 5000)
start = time.time()
total_factors = 0
with open('numbers.bin', 'r') as f:
    for line in f:
        num = int(line.strip())
        factors = prime_factors(num)
        total_factors += len(factors)
    f.close()
end = time.time()

print("Result: ", total_factors)
print("Time: ", end-start) #Time:  6.2814977169036865 sec