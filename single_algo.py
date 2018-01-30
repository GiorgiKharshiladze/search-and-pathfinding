from implement import *

count = 0

def _dfs(my_list, next_node):

	global count

	# Explain each member
	# i 			= next_node[0]
	# j 			= next_node[1]
	# discovery 	= next_node[2]
	# finish		= next_node[3]
	# state			= next_node[4]

	next_node[4] = "DISCOVERED"
	next_node[2] = count

	count += 1

	for node in directions(my_list, next_node):
		# node state
		if node[4] == "NEW":
			_dfs(my_list, node)

	next_node[4] = "FINISHED"
	next_node[3] = count

	count += 1

def dfs(my_list, start_node):

	global count

	count = 1

	_dfs(my_list, start_node)


