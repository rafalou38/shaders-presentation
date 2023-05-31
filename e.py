from hwcounter import Timer, count, count_end

from time import sleep
from math import sqrt


# 1. Manually count cycles elapsed between two points

start = count()
sqrt(144) / 12
elapsed = count_end() - start
print(f'elapsed cycles: {elapsed}')
# elapsed cycles: 36486


# 2. Use Timer object as context manager to wrap a block of code and measure its timing

with Timer() as t:
    sleep(1)
    print(f'elapsed cycles: {t.cycles}')
# elapsed cycles: 2912338344
