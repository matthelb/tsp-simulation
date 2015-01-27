import copy
import math
import os
import random

from tsp import TSP

def generate_simulation(num_cities, min_coord, max_coord, trials, directory):
	t = TSP()
	t.randomize(str(num_cities), num_cities, min_coord, max_coord)
	if not os.path.exists(directory):
		os.makedirs(directory)
	f = open(os.path.join(directory, '{0}.tsp'.format(num_cities)), 'w+')
	t.write(f)
	f.close()
	zero_padding = int(math.ceil(math.log10(trials)))
	a, b = random.sample(range(num_cities), 2)
	for i in range(trials):
		d = os.path.join(directory, str(i).zfill(zero_padding))
		if not os.path.exists(d):
			os.mkdir(d)
		t_i = copy.deepcopy(t)
		x_a_0, y_a_0 = t_i.replace_node(a, random.uniform(min_coord, max_coord), random.uniform(min_coord, max_coord))
		f = open(os.path.join(d, '{0}_a.tsp'.format(num_cities)), 'w+')
		t_i.write(f)
		f.close()
		x_a_1, y_a_1 = t_i.replace_node(a, x_a_0, y_a_0)
		t_i.replace_node(b, random.uniform(min_coord, max_coord), random.uniform(min_coord, max_coord))
		f = open(os.path.join(d, '{0}_b.tsp'.format(num_cities)), 'w+')
		t_i.write(f)
		f.close()
		t_i.replace_node(a, x_a_1, y_a_1)
		f = open(os.path.join(d, '{0}_ab.tsp'.format(num_cities)), 'w+')
		t_i.write(f)
		f.close()

PROCESSORS_PER_NODE = 8

def generate_pbs(tsp_file, processors, walltime, concorde_script, maxchunksize=16):
	f = open('{0}.pbs'.format(os.path.splitext(os.path.basename(tsp_file))[0]), 'w+')
	nodes = int(math.ceil(processors / PROCESSORS_PER_NODE))
	print('#!/bin/bash', file=f)
	print('#PBS -l nodes={0}:ppn={1}'.format(max(1, nodes), min(PROCESSORS_PER_NODE, processors)), file=f)
	print('#PBS -l walltime={0}'.format(walltime), file=f)
	if processors == 1:
		print('pbsdsh -v {0} 0 {1}'.format(concorde_script, maxchunksize), file=f)
	else:
		print('mpiexec -np 1 {0} 1 {1}'.format(concorde_script, maxchunksize), file=f)
