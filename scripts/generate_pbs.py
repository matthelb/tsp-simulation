import math
import sys

if len(sys.argv) != 9:
	print('Usage: {0} <num_cities> <max_coord> <iterations> <trials> <processors> <walltime> <exec_dir> <results_dir>'
				.format(sys.argv[0]), file=sys.stderr)
	sys.exit(1)

PROCESSORS_PER_NODE = 8

num_cities = int(sys.argv[1])
max_coord = float(sys.argv[2])
iterations = int(sys.argv[3])
trials = int(sys.argv[4])
processors = int(sys.argv[5])
walltime = sys.argv[6]
exec_dir = sys.argv[7]
results_dir = sys.argv[8]

results_dir += '/n{0}'.format(num_cities)
real_iterations = math.floor(iterations / processors)

for i in range(processors + 1):
	f = open('job{0}.pbs'.format(i), 'w+')
	print('#!/bin/bash', file=f)
	print('#PBS -l nodes=1:ppn=1', file=f)
	print('#PBS -l walltime={0}'.format(walltime), file=f)
	itrs = min(iterations - real_iterations * i, real_iterations)
	print('{0}/generate_tsp_csv {1} 0 {2} {3} {4}'.format(exec_dir, num_cities, max_coord, itrs, trials), file=f)
	f.close()
