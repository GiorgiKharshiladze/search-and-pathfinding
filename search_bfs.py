from maze import directions, start_point
import queue

queue = queue.Queue()
visited = []

def single_bfs(mylist, initial_node):

	visited.append([initial_node, None])

	queue.put(initial_node)

	while not queue.empty():

		parent_node = queue.get()

		i = parent_node[0]
		j = parent_node[1]

		if parent_node not in [elem[1] for elem in visited]:

			for next_node in directions(i, j):

				visited.append([list(next_node), list(parent_node)])

				if mylist[next_node[0]][next_node[1]] == ".":

					return visited

				else:

					queue.put(next_node)

	return False


# def get_path():


