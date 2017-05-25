'''
Author: Madhuri Palagummi
Date: 20-05-2017

Program: Find two elements whose sum is closest to zero
Reference: http://www.geeksforgeeks.org/two-elements-whose-sum-is-closest-to-zero/

'''

from merge_sort import merge_sort

def find_two_elements_sum_closest_to_zero(num_list):

    merge_sort(num_list, 0, len(num_list)-1)
    print num_list
    left_index = 0
    right_index = len(num_list)-1

    min_abs_sum = abs(num_list[left_index] + num_list[right_index])
    min_left_index = left_index
    min_right_index = right_index

    while left_index<right_index:

        sum = num_list[left_index] + num_list[right_index]
        abs_sum = abs(sum)

        if (abs_sum < min_abs_sum):
            min_abs_sum = abs_sum
            min_left_index = left_index
            min_right_index = right_index

        if (sum>0):
            right_index = right_index- 1
        elif sum == 0:
            return num_list[left_index], num_list[right_index]
        elif sum<0 :
            left_index = left_index + 1

    return num_list[min_left_index], num_list[min_right_index]

def main():
    num_list = [-1000, -999, 999, -800, 234, 799, 345]
    num_1, num_2 = find_two_elements_sum_closest_to_zero(num_list)
    print num_1, num_2

main()