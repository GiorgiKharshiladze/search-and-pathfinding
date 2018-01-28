from maze import read_maze, create_graph
from search import *


# MAIN
if __name__ == '__main__':
	
	listoflists = read_maze("text.txt")
	# listoflists = read_maze("lab-a/multiprize-tiny.txt")
	# listoflists = read_maze("lab-a/1prize-open.txt")

	for lst in listoflists:
		print(lst)

	print()
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



