def directions(mylist, i, j):

	my_dirs = []

	if mylist[i][j] != "%":
		# check north
		if mylist[i-1][j] != "%":
			my_dirs.append([i-1, j])
		# check east
		if mylist[i][j+1] != "%":
			my_dirs.append((i, j+1))
		#  check south
		if mylist[i+1][j] != "%":
			my_dirs.append((i+1, j))
		# check west
		if mylist[i][j-1] != "%":
			my_dirs.append((i, j-1))

	return my_dirs

def start_point(mylist):

	for i in range(0, len(mylist)):
		for j in range(0, len(mylist[i])):
			if(mylist[i][j] == "P"):
				return [i, j]