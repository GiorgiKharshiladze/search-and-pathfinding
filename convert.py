mylist = []

# Converts maze into a list of lists
def read_maze(file_name):

	file_name = open(file_name, "r")

	global mylist

	# Make mylist empty when this function runs
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

def show_graph():

	global mylist

	my_graph = {}

	for i in range(0, len(mylist)):
		for j in range(0, len(mylist[i])):
			if directions(i, j) != []:
				my_graph[(i, j)] = directions(i, j)

	return my_graph

# Remove '\n' at the end of the line
def rm_next_line(my_str):
	if(my_str.endswith('\n')):
		my_str = my_str[:-1]
	return my_str