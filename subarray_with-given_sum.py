'''
Author: Madhuri Palagummi
Date: 25-05-2017

Program: Subarray of non negative integers with given sum
Reference: http://www.geeksforgeeks.org/find-subarray-with-given-sum/

'''

def subarray_with_given_sum(num_list, target_sum):

    start = 0
    end = 0
    sum = num_list[0]

    while end<len(num_list):

        if (sum == target_sum):
            return start, end
        elif sum > target_sum and start!=end:
            sum = sum - num_list[start]
            start = start+1
        else:
            end = end + 1
            sum = sum + num_list[end]

    return None, None

def main():
    num_list = [1,1,1,1]

    start, end = subarray_with_given_sum(num_list, 20)
    print start, end

main()

