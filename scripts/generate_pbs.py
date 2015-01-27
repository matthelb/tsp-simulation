from __future__ import print_function

import math
import sys
import os

if len(sys.argv) != 19:
	print('Usage: {0} <run_script> <cairomm_path> <exec_file> <output_dir> <iterations> <min_coord> <max_coord> <trials> <input_file> <max_compute_time> <max_chunk_size> <processors> <processors_per_trial> <walltime> <pbs_output_dir> <concorde_exec> <mpi_wrapper_exec> <run_id_offset>'
				.format(sys.argv[0]), file=sys.stderr)
	sys.exit(1)

PROCESSORS_PER_NODE = 8

run_script = sys.argv[1]
cairomm_path = sys.argv[2]
exec_file = sys.argv[3]
output_dir = sys.argv[4]
iterations = int(sys.argv[5])
min_coord = float(sys.argv[6])
max_coord = float(sys.argv[7])
trials = int(sys.argv[8])
input_file = sys.argv[9]
max_compute_time = int(sys.argv[10])
max_chunk_size = int(sys.argv[11])
processors = int(sys.argv[12])
processors_per_trial = int(sys.argv[13])
walltime = sys.argv[14]
pbs_output_dir = sys.argv[15]
concorde_exec = sys.argv[16]
mpi_wrapper_exec = sys.argv[17]

nodes = int(math.ceil(processors / PROCESSORS_PER_NODE))
trial_groups = processors / processors_per_trial
trials_per_group = int(math.ceil(trials / trial_groups))

out_file = os.path.splitext(os.path.basename(input_file))[0]

f = open('{0}/{1}.pbs'.format(pbs_output_dir, out_file), 'w+')
print('#!/bin/bash', file=f)
print('#PBS -l nodes={0}:ppn={1}'.format(max(1, nodes), min(PROCESSORS_PER_NODE, processors)), file=f)
print('#PBS -l walltime={0}'.format(walltime), file=f)
for i in range(trial_groups):
	node = int(i * processors_per_trial / PROCESSORS_PER_NODE)
	trials_start = i * trials_per_group
	trials_end = (i + 1) * trials_per_group
	print('pbsdsh -v -n {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16}'.format(node, run_script, cairomm_path, exec_file, output_dir, iterations, min_coord, max_coord, trials_start, trials_end, input_file, max_compute_time, max_chunk_size, processors_per_trial, concorde_exec, mpi_wrapper_exec, i), file=f)
