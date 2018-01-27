# Remove '\n' at the end of the line
def rm_next_line(my_str):
	if(my_str.endswith('\n')):
		my_str = my_str[:-1]
	return my_str

# Converts maze into a list of lists
def read_maze(file_name):

	file_name = open(file_name, "r")

	mylist = []

	file = file_name.readlines()

	for i in range(0,len(file)):
		each_list = []

		# Remove '\n' at the end of the line
		file[i] = rm_next_line(file[i])

		for j in file[i]:
			each_list.append(j)

		mylist.append(each_list)

	return mylist

def directions(mylist, i, j):
	
	my_dirs = []

	if mylist[i][j] != "%":
		# check north
		if mylist[i-1][j] != "%":
			my_dirs.append((i-1, j))
		# check east
		if mylist[i][j+1] != "%":
			my_dirs.append((i, j+1))
		if mylist[i+1][j] != "%":
			my_dirs.append((i+1, j))
		if mylist[i][j-1] != "%":
			my_dirs.append((i, j-1))

	return my_dirs

def create_graph(mylist):

	my_graph = {}

	for i in range(0, len(mylist)):

		for j in range(0, len(mylist[i])):
			if directions(mylist, i, j) != []:
				my_graph[(i, j)] = directions(mylist, i, j)

	return my_graph

# MAIN
if __name__ == '__main__':
	
	listoflists = read_maze("text.txt")
	# listoflists = read_maze("lab-a/multiprize-tiny.txt")

	for lst in listoflists:
		print(lst)

	graph = create_graph(listoflists)

	for key, value in graph.items():
		print(key,":", value)


