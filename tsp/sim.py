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
