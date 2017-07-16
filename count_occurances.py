'''
Author: Madhuri Palagummi
Date: 20-05-2017

Program: Count number of occurances of a given element in sorted array

'''


def first_occurance_of_element(num_list, start_index, end_index, number):

    if start_index<end_index:
        mid_index = (end_index+start_index)/2

        if num_list[mid_index] == number:
            first_occurance = first_occurance_of_element(num_list, start_index, mid_index-1, number)
            if (first_occurance == -1):
                return mid_index

        elif num_list[mid_index] > number:
            return first_occurance_of_element(num_list, start_index, mid_index-1, number)

        else:
            return first_occurance_of_element(num_list, mid_index+1, end_index, number)

    else:
        return -1

def main():

    num_list = [1,1,2,3,4,4,4,4,4,5,6]
    first_occ = first_occurance_of_element(num_list, 0, len(num_list)-1, 4)
    print first_occ

main()


    


