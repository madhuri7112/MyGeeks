'''
Author: Madhuri Palagummi
Date: 18-05-2017

Program: Sort an array of 0s, 1s and 2s
Reference: http://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/

This solution uses Dutch national flag algo
'''

def segregate012(num_list):
    low_index = 0
    mid_index = 0
    high_index = len(num_list)-1

    while mid_index<=high_index:

        if num_list[mid_index] == 0:
            swap_values(num_list, mid_index, low_index)
            mid_index = mid_index+1
            low_index = low_index+1
        elif num_list[mid_index] == 1:
            mid_index = mid_index + 1
        elif num_list[mid_index] == 2:
            swap_values(num_list, mid_index, high_index)
            high_index = high_index -1


def swap_values(num_list, index_1, index_2):
    temp = num_list[index_1]
    num_list[index_1] = num_list[index_2]
    num_list[index_2] = temp

def main():
    num_list = [2,0,1,2,2,2,1,1,0,2]
    segregate012(num_list)
    print num_list

main()