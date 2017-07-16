'''
Author: Madhuri Palagummi
Date: 07-07-2017

Program: Odd frequency element
Reference: http://www.geeksforgeeks.org/find-the-number-occurring-odd-number-of-times/

'''

import sys

def find_odd_freq_element(list_numbers):

    xor_result = list_numbers[0]

    for num in list_numbers[1:]:
        xor_result = xor_result ^ num

    print xor_result

def main():

    if len(sys.argv)!=1:
        print "Please pass the list of nums as paramter"

    