"""
File: boggle.py
Name: Simon Lan
----------------------------------------
TODO:
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	TODO:
	"""
	board_lst = []
	while len(board_lst) < 4:
		# print(f'board: {board_lst}')
		s = input(str(len(board_lst)+1) + ' row of letters: ').lower().split()
		# print(f'current row: {s}')
		if len(s) == 4:
			temp = True
			for i in range(len(s)):
				if not s[i].isalpha() or len(s[i]) != 1:
					print('Illegal input')
					temp = False
					break
			if temp:
				board_lst.append(s)
		else:
			print('Illegal input')

	full_dict = read_dictionary()
	find_boggle(board_lst, full_dict)

	start = time.time()
	####################
	#                  #
	#       TODO:      #
	#                  #
	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		words = f.read().split()
		words_set = set(words)
	return words_set


def find_boggle(board_list, full_dict):
	ans_list = []
	for x in range(len(board_list)):
		for y in range(len(board_list)):
			find_boggle_helper(board_list, '', x, y, ans_list, [(x, y)], full_dict)
	print(f'There are {len(ans_list)} words in total.')


def find_boggle_helper(board_list, current_s, init_x, init_y, ans_list, index_lst, full_dict):
	if len(current_s) >= 4:
		if current_s in full_dict and current_s not in ans_list:
			ans_list.append(current_s)
			print(f'found "{current_s}"')
	for i in range(-1, 2):
		for j in range(-1, 2):
			new_x = init_x+i
			new_y = init_y+j
			neighbor = (new_x, new_y)
			# 確定neighbor是否in index_lst
			# 確定neighbor存在在板子上的座標位置，有存在才做choose/explore/un-choose
			if neighbor not in index_lst:
				if 0 <= new_x <= 3 and 0 <= new_y <= 3:
					# choose
					current_s += board_list[new_x][new_y]
					index_lst.append(neighbor)
					# explore
					if has_prefix(current_s, full_dict):
						find_boggle_helper(board_list, current_s, new_x, new_y, ans_list, index_lst, full_dict)
					# un-choose
					current_s = current_s[:len(current_s) - 1]
					index_lst.pop()


def has_prefix(sub_s, full_dict):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for ch in full_dict:
		if ch.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
