'''
Author: Madhuri Palagummi
Date: 07-05-2017

Program: Bubble Sort
Reference: http://www.geeksforgeeks.org/bubble-sort/
'''

def bubble_sort(num_list):
    """
     @function: bubble_sort
     @arg List num_list - List of numbers to be sorted

     @return List - List of sorted numbers
    """

    length = len(num_list)

    #No need of sorting if the array has no or one element
    if (length == 0 or length == 1):
        return num_list

    for start_index in range(0, length-1):

        #This flag will be set if there is atleast one swap during this iteration
        no_swap = True
        #print "start" + str(start_index)

        #After every iteration the max element will be pushed to the rightmost index, so ignore the rightmost pushed elemets
        for iterate_index in range(0, length-start_index-1):

            #print "iterate_index" + str(iterate_index)
            if (num_list[iterate_index + 1] < num_list[iterate_index]):
                temp = num_list[iterate_index]
                num_list[iterate_index] = num_list[iterate_index+1]
                num_list[iterate_index + 1] = temp
                no_swap = False
                #print num_list
        #If there is not even a single swap, it means all the numbers are sorted
        if no_swap:
            break;

    return num_list

def test_bubble_sort():
    '''
    Runs test cases for bubble sort
    '''

    test_list_1 = [4, 6, 8, 1, 9, 0]
    test_list_2 = [7, 12, 45, 24, 90, 7, 68]
    test_list_3 = [18, 13, 21, 34, 46, 90]

    print "list: " + str(test_list_1) + "sorted list: " + str(bubble_sort(test_list_1))
    print "list: " + str(test_list_2) + "sorted list: " + str(bubble_sort(test_list_2))
    print "list: " + str(test_list_3) + "sorted list: " + str(bubble_sort(test_list_3))


def main():
   test_bubble_sort()

if __name__ == '__main__':
    main()
