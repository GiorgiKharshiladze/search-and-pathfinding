
from implement import *
from heapq import *

pq = []
visited = {}

def multi_astar(mylist, start_node):
	cheese_amount = len(find_all_cheeses(mylist))
	cheese_list = find_all_cheeses(mylist)
	full_path = []

	visited[start_node] = (None, 0) # path cost is 0

	heappush(pq, get_priority_tuple(cheese_list, mylist, start_node))

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

				# if len(cheese_list) == 0:
				# 		return full_path

				if next_node in cheese_list:

					start_node = None
					if len(full_path) != 0:
						start_node = full_path[-1]

					full_path = full_path + multi_astar_path(mylist, visited, start_node, next_node)
					cheese_list.remove(next_node)

				heappush(pq, get_priority_tuple(cheese_list, mylist, next_node))

	return full_path

import math

def get_priority_tuple(cheese_list, mylist, node):

	min_weight = math.inf

	for next_goal in cheese_list:
		weight = math.sqrt((next_goal[1]-node[1])**2 + (next_goal[0]-node[0])**2)
		if weight < min_weight:
			min_weight = weight

	return (min_weight, node)

def multi_astar_path(mylist, visited, start_node, end_node):

	path = []

	last = end_node
	path.append(last)

	while True:
		parent = visited[last][0]
		if parent == start_node or parent == None:
			break
		path.append(parent)
		last = parent

	return path[::-1]
