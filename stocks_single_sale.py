#Author: Madhuri Palagummi
#Date: August 7 2017


def get_max_difference(list_of_nums):

   if  not len(list_of_nums) > 0:
     return 0

   start = list_of_nums[0]
   diff = 0

   for num in list_of_nums[1:]:
       if (num < start):
          start = num
          continue
       
       if (num - start > diff):
          diff = num - start

   return diff

def main():

    list_of_nums = []
    print get_max_difference(list_of_nums)

main()

