from __future__ import print_function

import random

class TSP:

	def __init__(self):
		self.name = ''
		self.comment = ''
		self.type = ''
		self.dimension = 0
		self.edge_weight_type = ''
		self.nodes = []

	def read(self, f):
		for line in f:
			key, value = [s.strip() for s in line.split(':')]
			if   key == 'NAME':
				self.name = value
			elif key == 'COMMENT':
				self.comment = value
			elif key == 'TYPE':
				self.type = value
			elif key == 'DIMENSION':
				self.dimension = int(v)
			elif key == 'EDGE_WEIGHT_TYPE':
				self.edge_weight_type = v
			elif key == 'NODE_COORD_SECTION':
				for i in range(self.dimension):
					n = f.next().split()
					self.nodes.append([float(n[1]), float(n[2])])


	def write(self, f):
		print('NAME: {0}'.format(self.name), file=f)
		print('COMMENT: {0}'.format(self.comment), file=f)
		print('TYPE: {0}'.format(self.type), file=f)
		print('DIMENSION: {0}'.format(self.dimension), file=f)
		print('EDGE_WEIGHT_TYPE: {0}'.format(self.edge_weight_type), file=f)
		print('NODE_COORD_SECTION:', file=f)
		for i in range(self.dimension):
			print('  {0} {1} {2}'.format(i + 1, self.nodes[i][0], self.nodes[i][1]), file=f)

	def randomize(self, name, num_cities, min_coord, max_coord):
		self.name = name
		self.type = 'TSP'
		self.dimension = num_cities
		self.edge_weight_type = 'EUC_2D'
		for i in range(self.dimension):
			self.nodes.append([random.uniform(min_coord, max_coord), random.uniform(min_coord, max_coord)])

	def replace_node(self, node, x_coord, y_coord):
		old_node = (self.nodes[node][0], self.nodes[node][1])
		self.nodes[node][0] = x_coord
		self.nodes[node][1] = y_coord
		return old_node
