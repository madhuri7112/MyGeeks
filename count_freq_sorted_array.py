def main():
   nums = [1, 1, 2, 2, 2, 2, 3]
   target = 3
   print count_frequency_in_sorted_array(nums, target)

def count_frequency_in_sorted_array(nums, target):

   first_occurance = search_first_occurance(nums, target,0 ,len(nums)-1)
   last_occurance = search_last_occurance(nums, target, 0, len(nums) - 1)
   frequency = last_occurance - first_occurance + 1

   return frequency

def search_first_occurance(nums, target, start_index, end_index):
   
    if (start_index > end_index):
        return -1
    mid = (start_index+end_index)/2
    if (nums[mid] > target):
       return search_first_occurance(nums, target, start_index, mid-1)
    elif (nums[mid] < target):
       return search_first_occurance(nums, target, mid+1, end_index)
    else:
       if (mid == 0 or nums[mid-1]!=target):
           return mid
       else:
           return search_first_occurance(nums, target, start_index, mid-1)
    
def search_last_occurance(nums, target, start_index, end_index):

   if (start_index > end_index):
      return -1
   mid = (start_index+end_index)/2
   if (nums[mid] > target):
       return search_last_occurance(nums, target, start_index, mid-1)
   elif (nums[mid] < target):
       return search_last_occurance(nums, target, mid+1, end_index)
   else:
      if(mid == len(nums) - 1 or nums[mid+1] != target):
         return mid
      else:
        return search_last_occurance(nums, target, mid+1, end_index)
main()

