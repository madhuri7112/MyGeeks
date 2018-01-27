import Queue as Q

def main():

    nums = [9, 8, 8, 5]
    k = 3
    print max_sum_after_k_negations(nums,k)
   
def max_sum_after_k_negations(nums, k):
     
     if (len(nums)==0):
        return 0

     q = Q.PriorityQueue()
     for num in nums:
        q.put(num)

     while(k>0):
         min_element = q.get()
         q.put(-1*min_element)
         k = k-1

     sum = 0 
     for num in list(q.queue):
       sum = sum + num

     return sum
    
main()     
