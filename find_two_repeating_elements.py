'''
Author: Madhuri Palagummi
Date: 20-05-2017

Program: Find two elements whose sum is closest to zero
Reference: http://www.geeksforgeeks.org/find-the-two-repeating-elements-in-a-given-array/

'''

def find_two_repeating_elements(num_list):

    for num in num_list:
        num_list[abs(num)] = -1*num_list[abs(num)]

    repeating_elements = []

    # Ignore 1st and last elements since their index is 0 and n+1
    for num in num_list[1:len(num_list)-1]:
        if num>0:
            repeating_elements.append(num)

    return repeating_elements


def main():
    num_list = [1,2,2,3,4,5,6,7,7]
    repeating_elements = find_two_repeating_elements(num_list)
    print repeating_elements

main()