from maze import read_maze, create_graph
from search import *

filename = "text.txt"
# filename = "lab-a/1prize-open.txt"
# filename = "lab-a/multiprize-tiny.txt"

# MAIN

def server_data():
	listoflists = read_maze(filename)
	return listoflists

if __name__ == '__main__':
	
	listoflists = read_maze(filename)

	for lst in listoflists:
		print(lst)

	print()

	# graph = create_graph()

	# for key, value in graph.items():
	# 	print(key,":", value)

	myPath = dfs((1,1))

	for i in range(0, len(listoflists)):
		for j in range(0, len(listoflists[i])):
			for z in range(0, len(myPath)):
				if ((i, j) == myPath[z]):
					listoflists[i][j] = str(z)

		
	for lst in listoflists:
		print(lst)



