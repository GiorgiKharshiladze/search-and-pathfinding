from maze import directions

visited = []
path = []
done = False

def _dfs(mylist, next_node):

	global visited, path, ans, done

	i = next_node[0]
	j = next_node[1]

	visited.append(next_node)
	path.append(next_node)

	if mylist[i][j] == ".":
		done = True

	for next_nbr in directions(i, j):

		if done:
			break

		while True:
			if path[-1] != next_node:
				del(path[-1])
			else:
				break

		if next_nbr not in visited:

			_dfs(mylist, next_nbr)


def dfs(mylist, next_node):

	global path

	_dfs(mylist, next_node)

	return path



