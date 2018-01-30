from maze import *
from search_dfs import *
from search_bfs import *

filename = "text.txt"
# filename = "lab-a/1prize-large.txt"
# filename = "lab-a/1prize-medium.txt"
# filename = "lab-a/1prize-open.txt"
# filename = "lab-a/multiprize-medium.txt"
# filename = "lab-a/multiprize-small.txt"
# filename = "lab-a/multiprize-tiny.txt"

listoflists = read_maze(filename)
# MAIN

def web_start_data():
	global listoflists

	return listoflists

def web_path_data():
	global listoflists

	start = tuple(start_point(listoflists))

	# only dfs
	my_path = dfs(listoflists, start)
 
	# Return converted my_path to list of lists
	return [list(elem) for elem in my_path]

if __name__ == '__main__':

	for lst in listoflists:
		print(lst)

	print()

	# print(single_bfs(listoflists, start_point(listoflists)))

	# graph = create_graph()

	# for key, value in graph.items():
	# 	print(key, " ", value)

	# Mouse position
	# start = tuple(start_point(listoflists))

	# my_path = dfs(listoflists, start)

	for i in range(0, len(listoflists)):
		for j in range(0, len(listoflists[i])):
			for z in range(0, len(my_path)):
				if ((i, j) == my_path[z]):
					listoflists[i][j] = str(z)

		
	# for lst in listoflists:
	# 	print(lst)

