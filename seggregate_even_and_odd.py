'''
Author: Madhuri Palagummi
Date: 25-05-2017

Program: Find two elements whose sum is closest to zero
Reference: http://www.geeksforgeeks.org/segregate-even-and-odd-numbers/

'''

def seggregate_even_and_odd(num_list):

    left_index = 0
    right_index = len(num_list) - 1

    while left_index<right_index and left_index<len(num_list) and right_index>=0:

        while num_list[left_index]%2 == 0 and left_index<len(num_list):
            left_index+=1

        while num_list[right_index]%2 != 0 and right_index>=0:
            right_index-=1

        temp = num_list[left_index]
        num_list[left_index] = num_list[right_index]
        num_list[right_index] = temp

        left_index+=1
        right_index-=1


def main():
    num_list = [22,21,23,25,62,24,13,15,24,28]
    seggregate_even_and_odd(num_list)

    print num_list

main()