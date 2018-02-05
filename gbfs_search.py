from implement import *
from heapq import *

pq = []
visited = []

def gbfs(mylist, start_node):

	visited.append([start_node, None])

	heappush(pq, get_priority_tuple(mylist, start_node))

	while pq:

		parent_node = heappop(pq)[1]

		i = parent_node[0]
		j = parent_node[1]

		if parent_node not in [elem[1] for elem in visited]:

			for next_node in directions(mylist, parent_node):

				visited.append([next_node, parent_node])

				if mylist[next_node[0]][next_node[1]] == ".":

					return gbfs_path(visited)

				else:

					heappush(pq, get_priority_tuple(mylist, next_node))

	return False

def get_priority_tuple(mylist, node):
	
	my_goal = find_cheese(mylist)

	weight = abs(my_goal[1]-node[1]) + abs(my_goal[0]-node[0])

	return (weight, node)

def gbfs_path(visited):

	path = []
	last = visited[-1][0]
	last_parent = visited[-1][1]

	path.append(last)
	path.append(last_parent)

	for i in visited[::-1]:

		if i[0] == last_parent and i[1] != None:
			path.append(i[1])
			last_parent = i[1]

	return path[::-1], visited
