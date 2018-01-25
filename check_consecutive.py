def main():
     nums = [1,3,4,3]
     is_consecutive = check_consecutive(nums)
     print is_consecutive
 
def check_consecutive(nums):
    min = nums[0]
    max = nums[0]

    for num in nums:
        if num<min:
           min = num

        if num>max:
           max = num

    if ((max-min+1)!= len(nums)):
        return False

    for num in nums:
        if (nums[abs(num) - min]<0):
            return False
        nums[abs(num) - min] = -1*nums[abs(num) - min] 


    for num in nums:
       if (num>0):
          return False

    return True


main()
