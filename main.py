from convert import *
from single_algo import *
from implement import *


filename = "lab-a/test.txt"
# filename = "lab-a/1prize-large.txt"
# filename = "lab-a/1prize-medium.txt"
# filename = "lab-a/1prize-open.txt"
# filename = "lab-a/multiprize-medium.txt"
# filename = "lab-a/multiprize-small.txt"
# filename = "lab-a/multiprize-tiny.txt"

my_list = read_maze(filename)


def maze_data():

	global my_list

	return my_list

def mouse_path():

	start_position = find_mouse(my_list)
	goal_position = find_cheese(my_list)

	my_graph = show_graph(my_list)

	my_path = list(dfs_paths(my_graph, start_position, goal_position))

	return [list(elem) for elem in my_path]



if __name__ == '__main__':

	for line in my_list:
		print(line)

	start_position = find_mouse(my_list)
	goal_position = find_cheese(my_list)

	my_graph = show_graph(my_list)

	print(list(bfs_paths(my_graph, start_position, goal_position)))
