from convert import *
from implement import *
from dfs_search import dfs
from bfs_search import bfs
from gbfs_search import gbfs
from astar_search import astar
from multi_astar_search import m_astar


# filename = "lab-a/test.txt"
# filename = "lab-a/1prize-large.txt"
# filename = "lab-a/1prize-medium.txt"
# filename = "lab-a/1prize-open.txt"
filename = "lab-a/multiprize-medium.txt"
# filename = "lab-a/multiprize-small.txt"
# filename = "lab-a/multiprize-tiny.txt"



def maze_data(filename):

	my_list = read_maze(filename)

	return my_list

def mouse_path(filename):

	my_list = read_maze(filename)

	start_position = find_mouse(my_list)

	my_path = list(multi_astar(my_list, start_position))

	return [list(elem) for elem in my_path]

def display_result_multi(my_list, final_path):

	print("Path Cost:", len(final_path[0]))
	print("Number of nodes expanded:", len(final_path[1]))

	counter = 1
	let_counter = "A"
	for next_node in final_path[0][:-1]:
		i = next_node[0]
		j = next_node[1]
		my_list[i][j] = "#"
		if (i,j) in find_all_cheeses(my_list):
			my_list[i][j] = counter
			counter += 1
			# if counter > 9:
			# 	my_list[i][j] = let_counter
			# 	let_counter += 1

	my_maze = ""
	for line in my_list:
		myline = ""
		for item in line:
			myline += item
		my_maze += myline+"\n"

	return my_maze

def display_result(my_list, final_path):

	print("Path Cost:", len(final_path[0]))
	print("Number of nodes expanded:", len(final_path[1]))

	

	for next_node in final_path[0][:-1]:
		i = next_node[0]
		j = next_node[1]
		my_list[i][j] = "#"

	final_path[0][-1] = "0"

	my_maze = ""
	for line in my_list:
		myline = ""
		for item in line:
			myline += item
		my_maze += myline+"\n"

	return my_maze

def single_dfs(filename):

	my_list = read_maze(filename)
	
	start_position = find_mouse(my_list)

	final_path = dfs(my_list, start_position)

	return display_result(my_list, final_path)

def single_bfs(filename):

	my_list = read_maze(filename)
	
	start_position = find_mouse(my_list)

	final_path = bfs(my_list, start_position)

	return display_result(my_list, final_path)

def single_gbfs(filename):

	my_list = read_maze(filename)
	
	start_position = find_mouse(my_list)

	final_path = gbfs(my_list, start_position)

	return display_result(my_list, final_path)

def single_astar(filename):

	my_list = read_maze(filename)
	
	start_position = find_mouse(my_list)

	final_path = gbfs(my_list, start_position)

	return display_result(my_list, final_path)

def multi_astar(filename):

	my_list = read_maze(filename)
	
	start_position = find_mouse(my_list)

	final_path = m_astar(my_list, start_position)

	return display_result_multi(my_list, final_path)



if __name__ == '__main__':

	print(multi_astar(filename))

