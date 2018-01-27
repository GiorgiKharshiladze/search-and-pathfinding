def rm_next_line(my_str):
	if(my_str.endswith('\n')):
		my_str = my_str[:-1]
	return my_str


def main():

	file_open = open("text.txt", "r")

	mylist = []

	file = file_open.readlines()

	for i in range(0,len(file)):
		each_list = []

		# Remove '\n' at the end of the line
		file[i] = rm_next_line(file[i])

		for j in file[i]:
			each_list.append(j)

		mylist.append(each_list)

	return mylist

# MAIN

listoflists = main()

for lst in listoflists:
	print(lst)