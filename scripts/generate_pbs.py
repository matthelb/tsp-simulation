from __future__ import print_function

import math
import sys

if len(sys.argv) != 14:
	print('Usage: {0} <num_cities> <min_coord> <max_coord> <trials> <processors> <walltime> <exec_dir> <results_dir> <input_file> <cairomm_path> <output_dir> <maxchunksize> <run_script>'
				.format(sys.argv[0]), file=sys.stderr)
	sys.exit(1)

PROCESSORS_PER_NODE = 8

num_cities = int(sys.argv[1])
min_coord = float(sys.argv[2])
max_coord = float(sys.argv[3])
trials = int(sys.argv[4])
processors = int(sys.argv[5])
walltime = sys.argv[6]
exec_dir = sys.argv[7]
results_dir = sys.argv[8]
input_file = sys.argv[9]
cairomm_path = sys.argv[10]
output_dir = sys.argv[11]
maxchunksize = int(sys.argv[12])
run_script = sys.argv[13]

nodes = int(math.ceil(processors / PROCESSORS_PER_NODE))
real_trials = int(trials / processors)

f = open('{0}/job{1}.pbs'.format(output_dir, num_cities), 'w+')
print('#!/bin/bash', file=f)
print('#PBS -l nodes={0}:ppn={1}'.format(max(1, nodes), min(PROCESSORS_PER_NODE, processors)), file=f)
print('#PBS -l walltime={0}'.format(walltime), file=f)
for i in range(processors):
	trial_start = int(i * real_trials)
	trial_end = int(min((i + 1) * real_trials, trials))
	print('pbsdsh -n {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} &'.format(i, run_script, cairomm_path, exec_dir, results_dir, 1, min_coord, max_coord, trial_start, trial_end, input_file, i, 0, maxchunksize), file=f)
f.close()

# for i in range(processors + 1):
# 	f = open('{0}/job{1}_{2}.pbs'.format(output_dir, str(i).zfill(int(math.log10(processors)) + 1), num_cities), 'w+')
# 	print('#!/bin/bash', file=f)
# 	print('#PBS -l nodes=1:ppn=1', file=f)
# 	print('#PBS -l walltime={0}'.format(walltime), file=f)
# 	trial_start = int(i * real_trials)
# 	trial_end = int(min((i + 1) * real_trials, trials))
# 	print('export LD_LIBRARY_PATH="{0}:$LD_LIBRARY_PATH"'.format(cairomm_path), file=f)
# 	print('{0}/generate_tsp_csv {1} {2} {3} {4} {5} {6} {7} {8}'.format(exec_dir, results_dir, 1, min_coord, max_coord, trial_start, trial_end, input_file, i), file=f)
# 	f.close()
