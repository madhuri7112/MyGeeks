'''
Author: Madhuri Palagummi
Date: 11-05-2017

Program: Insert sort
Reference: http://www.geeksforgeeks.org/insertion-sort/
'''
def insertionSort(num_list):

    for current_pointer in range(1, len(num_list) - 1):

        current_pointer_value = num_list[index]

        for position in range(current_pointer, 0, -1):

