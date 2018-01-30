from main import my_list

# Show all the NESW directions of node
def directions(node):

	# i and j position in the list of lists
	i = node[0]
	j = node[1]

	# Empty list of all the directions
	my_dirs = []

	global my_list

	if my_list[i][j] != "%":
		# check north
		if my_list[i-1][j] != "%":
			my_dirs.append([i-1, j])
		# check east
		if my_list[i][j+1] != "%":
			my_dirs.append([i, j+1])
		#  check south
		if my_list[i+1][j] != "%":
			my_dirs.append([i+1, j])
		# check west
		if my_list[i][j-1] != "%":
			my_dirs.append([i, j-1])

	return my_dirs

# Return the starting position of Mouse
def start_pos():

	global my_list

	for i in range(0, len(my_list)):
		for j in range(0, len(my_list[i])):
			if(my_list[i][j] == "P"):
				return [i, j]