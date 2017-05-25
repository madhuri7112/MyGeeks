'''
Author: Madhuri Palagummi
Date: 20-05-2017

Program: Merge sort
Reference:   http://www.geeksforgeeks.org/merge-sort/

'''

import math

def merge(num_list, lowest_index, mid_index, highest_index):

    temp_left_array = []
    temp_right_array = []
    for i in range(lowest_index, mid_index+1):
        temp_left_array.append(num_list[i])

    for i in range(mid_index+1, highest_index+1):
        temp_right_array.append(num_list[i])

    left_array_index = 0
    right_array_index = 0
    num_list_index = lowest_index

    while left_array_index<len(temp_left_array) and right_array_index<len(temp_right_array):

        if temp_left_array[left_array_index] <= temp_right_array[right_array_index]:
            num_list[num_list_index] = temp_left_array[left_array_index]
            left_array_index += 1
        else:
            num_list[num_list_index] = temp_right_array[right_array_index]
            right_array_index = right_array_index + 1

        num_list_index += 1

    if left_array_index<len(temp_left_array):

        for num in temp_left_array[left_array_index:]:
            num_list[num_list_index] = num
            num_list_index += 1

    if right_array_index<len(temp_right_array):

        for num in temp_right_array[right_array_index:]:

            num_list[num_list_index] = num
            num_list_index += 1


def merge_sort(num_list, lowest_index, highest_index):

    if lowest_index<highest_index:

        mid_index = (highest_index+lowest_index)/2

        merge_sort(num_list, lowest_index, mid_index)
        merge_sort(num_list, mid_index+1, highest_index)
        merge(num_list, lowest_index, mid_index, highest_index)



def main():
    num_list = [3,1,7,4,2,1,12,21,18,13]
    merge_sort(num_list, 0, len(num_list)-1)

    print num_list, "Sorted array"

if (__name__ == '__main__'):
    main()