from implement import *
from heapq import *

pq = []
visited = {}

def astar(mylist, start_node):

	visited[start_node] = (None, 0) # path cost is 0

	heappush(pq, get_priority_tuple(mylist, start_node))

	while pq:

		parent_node = heappop(pq)[1]

		i = parent_node[0]
		j = parent_node[1]

		for next_node in directions(mylist, parent_node):

			if next_node in visited.keys():

				parent_cost = visited[parent_node][1]
				next_node_cost = visited[next_node][1]

				if parent_cost + 1 < next_node_cost:
					visited[next_node] = (parent_node, parent_cost + 1)

			else:

				visited[next_node] = (parent_node, visited[parent_node][1] + 1)

				if mylist[next_node[0]][next_node[1]] == ".":

					return astar_path(mylist, visited), visited

				else:
					heappush(pq, get_priority_tuple(mylist, next_node))

	return False

import math

def get_priority_tuple(mylist, node):
	global visited

	my_goal = find_cheese(mylist)

	hypotenuse = math.sqrt((my_goal[1]-node[1])**2 + (my_goal[0]-node[0])**2)

	cost = visited[node][1]

	weight = hypotenuse + cost

	return (weight, node)

def astar_path(mylist, visited):

	path = []

	last = find_cheese(mylist)
	path.append(last)

	while True:
		parent = visited[last][0]
		if parent == None:
			break
		path.append(parent)
		last = parent

	return path[::-1]

