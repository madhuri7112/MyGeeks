'''
Author: Madhuri Palagummi
Date: 21-06-2017

Program: Smallest subarray with sum greater than a given value
Reference: http://www.geeksforgeeks.org/minimum-length-subarray-sum-greater-given-value/

'''

def find_min_subarray_with_sum_greater_than(num_list, target_sum):

    start = 0
    end = 0
    min_start = None
    min_end = None
    min_length = len(num_list) + 1
    sum = num_list[0]

    while end<len(num_list):

         if (sum <= target_sum) :
             end = end+1
             sum = sum + num_list[end]
         elif :

             if (end-start+1 > min_length):
                 min_length = end-start+1
                 min_start = start
                 min_end = end

             sum = sum - num_list[start]
             start = start + 1









