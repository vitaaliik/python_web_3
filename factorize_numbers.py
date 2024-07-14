import multiprocessing
import time

def factorize_number(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    with multiprocessing.Pool() as pool:
        result = pool.map(factorize_number, numbers)
    return result

def factorize_sync(*numbers):
    result = []
    for number in numbers:
        factors = []
        for i in range(1, number + 1):
            if number % i == 0:
                factors.append(i)
        result.append(factors)
    return result

if __name__ == "__main__":
    numbers = (128, 255, 99999, 10651060)

    print("Synchronous factorization:")
    start_time = time.time()
    result = factorize_sync(*numbers)
    end_time = time.time()
    for number, factors in zip(numbers, result):
        print(f"Factors of {number}: {factors}")
    print(f"Time taken: {end_time - start_time} seconds\n")

    print("Parallel factorization:")
    start_time = time.time()
    result = factorize(*numbers)
    end_time = time.time()
    for number, factors in zip(numbers, result):
        print(f"Factors of {number}: {factors}")
    print(f"Time taken: {end_time - start_time} seconds")
