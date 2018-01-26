import Queue as Q

def main():
  nums = [11, 8, 5, 7, 5, 100]
  k = 4
  print min_k_product(nums, k)
  
def min_k_product(nums, k):
    q = Q.PriorityQueue()
    
    for num in nums:
       q.put(num)
    
    if k > len(nums): 
       return -1
   
    product = 1
    for i in range(1, k+1):
       product = product * q.get()

    return product

main()

