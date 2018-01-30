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
			my_dirs.append([i-1, j, 0, 0, "NEW"])
		# check east
		if my_list[i][j+1] != "%":
			my_dirs.append([i, j+1, 0, 0, "NEW"])
		#  check south
		if my_list[i+1][j] != "%":
			my_dirs.append([i+1, j, 0, 0, "NEW"])
		# check west
		if my_list[i][j-1] != "%":
			my_dirs.append([i, j-1, 0, 0, "NEW"])

	return my_dirs

# Return the starting position of Mouse
def start_pos(my_list):

	for i in range(0, len(my_list)):
		for j in range(0, len(my_list[i])):
			if(my_list[i][j] == "P"):
				return [i, j, 0, 0, "NEW"]