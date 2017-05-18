'''
Author: Madhuri Palagummi
Date: 18-05-2017

Program: Maximum sum such that no two elements are adjacent
Reference: http://www.geeksforgeeks.org/maximum-sum-such-that-no-two-elements-are-adjacent/

'''


def find_max_sum(num_array):

    if (len(num_array) == 0):
        return 0

    if (len(num_array) == 1):
        return num_array[0]

    sum_including_current_element = num_array[0]
    sum_excluding_current_element = 0

    for num in num_array[1:]:

        sum_including_previous_element = sum_including_current_element
        sum_excluding_previous_element = sum_excluding_current_element

        sum_including_current_element = sum_excluding_previous_element+num
        sum_excluding_current_element = max(sum_including_previous_element, sum_excluding_previous_element)

        print sum_including_current_element, sum_excluding_current_element

    final_max_sum = max(sum_including_current_element, sum_excluding_current_element)

    return final_max_sum

def main():
    num_array = [5, 5, 10, 100, 10, 5]
    print find_max_sum(num_array)

main()