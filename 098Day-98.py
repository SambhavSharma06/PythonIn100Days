# MultiProcessing in Python!!
import time

from multiprocessing import Pool

def count(n):
    return n

if __name__ == "__main__":
    numbers = list(range(1, 1001))

    with Pool(4) as p:  # 4 processes
        result = p.map(count, numbers)

    print(result)
