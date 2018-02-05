from implement import *
import queue

queue = queue.Queue()
visited = []

def bfs(mylist, start_node):

	visited.append([start_node, None])

	queue.put(start_node)

	while not queue.empty():

		parent_node = queue.get()

		i = parent_node[0]
		j = parent_node[1]

		if parent_node not in [elem[1] for elem in visited]:

			for next_node in directions(mylist, parent_node):

				visited.append([next_node, parent_node])

				if mylist[next_node[0]][next_node[1]] == ".":

					return bfs_path(visited), visited

				else:

					queue.put(next_node)

	return False


def bfs_path(visited):

	path = []
	last = visited[-1][0]
	last_parent = visited[-1][1]

	path.append(last)
	path.append(last_parent)

	for i in visited[::-1]:

		if i[0] == last_parent and i[1] != None:
			path.append(i[1])
			last_parent = i[1]

	return path[::-1]
