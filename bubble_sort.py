num_list = [2]

def bubble_sort(num_list):
    length = len(num_list)

    if (length == 0 or length == 1):
        return num_list

    swapped = True

    while (swapped):
        swapped = False
        for i in range(0,length-1):
            if (num_list[i+1] < num_list[i]):
                temp = num_list[i];
                num_list[i] = num_list[i+1]
                num_list[i+1] = temp
                swapped = True

    return num_list

num_list = bubble_sort(num_list)
print num_list





