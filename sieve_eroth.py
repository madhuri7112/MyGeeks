
def main():
    sieve(10)

def sieve(n):

    nums = []
    for i in range(2, n+1):
      nums.append(i)

    p = find_next_non_marked(nums,0)
    while p!=-1:
      #print p
      if (2*p>n):
        break
      q = p+p
      while q<=n:
         #print q
         if (nums[q-2]>0):
            nums[q-2] = -1*nums[q-2]
         q = q+p
      p = find_next_non_marked(nums, p)

    for num in nums:
       if num>0:
        print num
    
def find_next_non_marked(nums, p):
    #print p 
    for num in nums:
       if num>0 and num>p:
          return num

    return -1

main()      
