'''
Author: Madhuri Palagummi
Date: 25-05-2017

Program: Equilibrium indexy
Reference: http://www.geeksforgeeks.org/equilibrium-index-of-an-array/

'''


def compute_sum_of_list(num_list):
    sum = 0
    for num in num_list:
        sum += num

    return sum

def find_equilibrium_indices(num_list):

    total_sum = compute_sum_of_list(num_list)
    equilibrium_indices = []

    for index, num in enumerate(num_list):

        if (index == 0):
            sum_left = 0
        else:
            sum_left = sum_left + num_list[index-1]

        sum_right = total_sum - num - sum_left

        if (sum_left == sum_right):
            equilibrium_indices.append(index)

    return equilibrium_indices

def main():

    num_array = [-7, 1, 5, 2, -4, 3, 0]
    equilibrium_indices = find_equilibrium_indices(num_array)

    print equilibrium_indices

main()