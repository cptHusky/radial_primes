import time
import math


def polar_to_descartes(r, fi):
    x = r * math.cos(fi)
    y = r * math.sin(fi)
    coordinates = (x, y)
    return coordinates


def prime_gen(limit):
    t = time.time()
    number = 1
    counter = 1
    primes = [2, ]
    while number < limit:
        number += 2
        is_prime = True
        for n in range(counter):
            if number % primes[n] == 0:
                is_prime = False
        if is_prime:
            primes.append(number)
            counter += 1
            print(f'{number} is prime')
    print(time.time() - t)
    return primes
