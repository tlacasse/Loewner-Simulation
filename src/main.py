import loewner as lw
import time

sim = lw.LESimulation('t', 20, 10000)

start = time.time()

hull = sim.compute_hull()

stop = time.time()

for i in hull:
    print(i)

print('Computation Time:', stop - start)
