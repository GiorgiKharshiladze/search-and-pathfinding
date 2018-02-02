
class PathNode:

	def __init__(self, value, position):

		self.value = value
		self.position = position

		self.directions = list()
		self.discovery  = 0
		self.finish     = 0
		self.state      = "new"

	def add_direction(self, next_position):

		directions_set = set(self.directions)

		if next_position not in directions_set:

			self.directions.append(next_position)
			self.directions.sort()


class MazeGraph:

	path_nodes = {}
	time = 0

	def add_path_node(self, path_node):

		if isinstance(path_node, PathNode) and path_node.position not in self.path_nodes:

			self.path_nodes[path_node.position] = path_node

			return True

		else:

			return False

	def add_path(self, position_one, position_two):

		if position_one in self.path_nodes and position_two in self.path_nodes:

			for from_node, to_node in self.path_nodes.items():
				if from_node == position_one:
					to_node.add_path(position_two)
				if from_node == position_two:
					to_node.add_path(position_one)

			return True

		else:
			return False

	def _dfs(self, path_node):

		global count

		path_node.state = "discovered"
		path_node.discovery = count
		count += 1

		for next_pos in path_node.directions():
			if self.path_nodes[path_node].state == "new":
				self._dfs(self.path_nodes(path_node))

		path_node.state  = "finished"
		path_node.finish = count
		count += 1

	def dfs(self, path_node):
		global count
		count = 1
		self._dfs(path_node)		


# Show all the NESW directions of node
def directions(my_list, node):

	# i and j position in the list of lists
	i = node[0]
	j = node[1]

	# Empty list of all the directions
	my_dirs = []

	# Each aember of my_dirs consists of a list ["position i", "position j", "discovery time", "finish time", "state: New, Discovered, Finished"]

	if my_list[i][j] != "%":
		# check north
		if my_list[i-1][j] != "%":
			my_dirs.append((i-1, j))
		# check east
		if my_list[i][j+1] != "%":
			my_dirs.append((i, j+1))
		#  check south
		if my_list[i+1][j] != "%":
			my_dirs.append((i+1, j))
		# check west
		if my_list[i][j-1] != "%":
			my_dirs.append((i, j-1))

	return my_dirs


def show_graph(mylist):

	my_graph = {}

	for i in range(0, len(mylist)):

		for j in range(0, len(mylist[i])):
			if directions(mylist, (i, j)) != []:
				my_graph[(i, j)] = set(directions(mylist, (i, j)))

	return my_graph

# Return the starting position of Mouse
def find_mouse(my_list):

	for i in range(0, len(my_list)):
		for j in range(0, len(my_list[i])):
			if(my_list[i][j] == "P"):
				return (i, j)

# Return the starting position of Cheese
def find_cheese(my_list):

	for i in range(0, len(my_list)):
		for j in range(0, len(my_list[i])):
			if(my_list[i][j] == "."):
				return (i, j)