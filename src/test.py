# -*- coding: utf-8 -*-
import time
import cmath

start = time.time()

for i in range(10000000):
    x = cmath.sqrt((2 + 3j) * (2 + 3j)) + (5 + 4j)

stop = time.time()

print('Computation Time:', stop - start)

