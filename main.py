from convert import *
from implement import *



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

	print(start_pos())