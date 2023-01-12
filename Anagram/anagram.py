"""
File: anagram.py
Name: Simon Lan
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        s = str(input("Find anagrams for: ")).lower()
        if s == EXIT:
            break
        start = time.time()
        full_dict = read_dictionary()
        ans_lst = []
        find_anagrams(s, full_dict, ans_lst)
        for i in range(len(ans_lst)):
            print("Found:  " + ans_lst[i])
            print("Searching...")

        print(f'{len(ans_lst)} anagrams: {ans_lst}')

        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        lines = f.readlines()
        lst = []
        for line in lines:
            temp = line.replace('\n', '')
            lst.append(temp)
        return lst


def find_anagrams(s, full_dict, ans_list):
    """
    :param:
    :return:
    """
    print("Searching...")
    find_anagrams_helper(s, "", len(s), ans_list, [], full_dict)


def find_anagrams_helper(s, current_s, ans_len, full_lst, index_list, full_dict):
    if len(current_s) == ans_len:
        if current_s in full_dict and current_s not in full_lst:
            full_lst.append(current_s)
    else:
        for i in range(len(s)):
            if i not in index_list:
                # choose
                current_s += s[i]
                index_list.append(i)
                # explore
                if has_prefix(current_s, full_dict):
                    find_anagrams_helper(s, current_s, ans_len, full_lst, index_list, full_dict)
                # un-choose
                current_s = current_s[:len(current_s)-1]
                index_list.pop()


def has_prefix(sub_s, full_dict):
    """
    :param sub_s:
    :return:
    """
    for ch in full_dict:
        if ch.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
