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

def goal_test(my_list):

	return bool(find_cheese(my_list))


def show_graph(my_list):

	my_graph = {}

	for i in range(0, len(my_list)):

		for j in range(0, len(my_list[i])):
			if directions(my_list, (i, j)) != []:
				my_graph[(i, j)] = set(directions(my_list, (i, j)))

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