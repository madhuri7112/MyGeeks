'''
Author: Madhuri Palagummi
Date: 25-05-2017

Program: Find fixed point in sorted array
Reference: http://www.geeksforgeeks.org/find-a-fixed-point-in-a-given-array/

'''

def find_fixed_point(num_list, start_index, end_index):

    if start_index<end_index:
        mid_index = (end_index + start_index)/2

        if num_list[mid_index] > mid_index:
            return find_fixed_point(num_list, start_index, mid_index)
        elif num_list[mid_index] < mid_index:
            return find_fixed_point(num_list, mid_index+1, end_index)
        else:
            return mid_index

    return None


def main():
    num_list = [ 0, 1, 2, 3, 4, 5, 6, 7]
    num_list = [-4,-3, 2, 6, 8, 10, 11, 12]
    ind = find_fixed_point(num_list, 0, len(num_list)-1)

    print  "Fixed point index: ", ind

main()

