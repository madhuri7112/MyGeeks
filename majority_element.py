'''
Author: Madhuri Palagummi
Date: 07-05-2017

Program: Majority element
Reference: http://www.geeksforgeeks.org/majority-element/

This solution uses Moore's algorithm
'''


def get_candidate_element(input_array):

    maj_index = 0
    maj_element = input_array[0]
    count = 1
    for index, number in enumerate(input_array, start=1):
        if number == maj_element:
            count = count+1
        else:
            if count==0:
                maj_index = index
                maj_element = number
                count = 1
            else:
                count = count-1
    return maj_element

def check_if_candidate_is_majority(candidate_element, input_array):

    count = 0
    for num in input_array:
        if num==candidate_element:
            count = count+1

    if (count > len(input_array)/2):
       return True

def get_majority_element(input_array):
    candidate_element = get_candidate_element(input_array)

    if (check_if_candidate_is_majority(candidate_element, input_array)):
        return candidate_element
    else:
        print "No majority element found"
        return None


def main():
    num_array = [2,2,3,4]

    print get_majority_element(num_array)

main()