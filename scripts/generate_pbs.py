from __future__ import print_function

import math
import sys

if len(sys.argv) != 10:
	print('Usage: {0} <min_coord> <max_coord> <trials> <processors> <walltime> <exec_dir> <results_dir> <input_file> <cairomm_path>'
				.format(sys.argv[0]), file=sys.stderr)
	sys.exit(1)

PROCESSORS_PER_NODE = 8

min_coord = float(sys.argv[1])
max_coord = float(sys.argv[2])
trials = int(sys.argv[3])
processors = int(sys.argv[4])
walltime = sys.argv[5]
exec_dir = sys.argv[6]
results_dir = sys.argv[7]
input_file = sys.argv[8]
cairomm_path = sys.argv[9]

real_trials = math.floor(trials / processors)

for i in range(processors + 1):
	f = open('job{0}.pbs'.format(i), 'w+')
	print('#!/bin/bash', file=f)
	print('#PBS -l nodes=1:ppn=1', file=f)
	print('#PBS -l walltime={0}'.format(walltime), file=f)
	trial_start = i * real_trials
	trial_end = min((i + 1) * real_trials, trials)
	print('export LD_LIBRARY_PATH="{0}:$LD_LIBRARY_PATH"'.format(cairomm_path), file=f)
	print('{0}/generate_tsp_csv {1} {2} {3} {4} {5} {6} {7} {8}'.format(exec_dir, results_dir, 1, min_coord, max_coord, trial_start, trial_end, input_file, i), file=f)
	f.close()
