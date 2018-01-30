from convert import *
from single_algo import *



filename = "lab-a/test.txt"
# filename = "lab-a/1prize-large.txt"
# filename = "lab-a/1prize-medium.txt"
# filename = "lab-a/1prize-open.txt"
# filename = "lab-a/multiprize-medium.txt"
# filename = "lab-a/multiprize-small.txt"
# filename = "lab-a/multiprize-tiny.txt"

my_list = read_maze(filename)


if __name__ == '__main__':

	for line in my_list:
		print(line)

	start_position = start_pos(my_list)

	# print(directions(my_list, start_position))

	# print(dfs(my_list, start_position))

	print(show_graph(my_list))