def main():
     n = 25
     print ludic_numbers(n)

def ludic_numbers(n):

       nums = []
       ludic_nums = [1]
       
       for n in range(2, n+1):
         nums.append(n)
       
       it = 2
       while (1):
          ludic_nums.append(nums[0])
          remove_index = 0
          while remove_index<len(nums):
               nums[remove_index] = -1
               remove_index = remove_index+it
          for ind,num in enumerate(nums):
              if num == -1:
                 nums.pop(ind)
          if len(nums) >0:
             it = nums[0]
          else:
             break
       
       return ludic_nums
 
main()    
     
    

