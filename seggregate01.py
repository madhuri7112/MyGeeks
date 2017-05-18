'''
Author: Madhuri Palagummi
Date: 18-05-2017

Program: Sort an array of 0s, 1s
Reference: http://www.geeksforgeeks.org/?p=5234

This solution uses Dutch national flag algo
'''

def seggregate01(num_list):
    low_index = 0
    high_index = len(num_list)-1

    while low_index <= high_index:
        if num_list[low_index] == 0:
            low_index = low_index + 1
        elif num_list[low_index] == 1:
            swap_values(num_list, low_index, high_index)
            high_index = high_index - 1

def swap_values(num_list, index_1, index_2):
    temp = num_list[index_1]
    num_list[index_1] = num_list[index_2]
    num_list[index_2] = temp

def main():
    num_list = [0,1,0,0,0,1,1,0,1]
    seggregate01(num_list)
    print num_list

main()