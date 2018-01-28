def main():
    nums = [2, 5, 3, 5, 4, 4, 2, 3]
    num_1 = 3
    num_2 = 2
    print find_min_distance(nums, num_1, num_2)


def find_min_distance(nums, num_1, num_2):
    
    min_dist = len(nums)+1
    number_found = None
    number_found_index = None

    for index, num in enumerate(nums): 
       #Set the first occurance 
       if number_found == None and (num == num_1 or num == num_2):
           number_found = num
           number_found_index = index
       elif num == number_found:
            number_found_index = index
       elif num == num_1 or num == num_2:
            dist = index - number_found_index
            if (dist<min_dist):
                 min_dist = dist
            number_found = num
            number_found_index = index
     
    return min_dist      
 
main()
       


    
