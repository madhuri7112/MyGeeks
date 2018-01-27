import Queue as Q

#https://www.geeksforgeeks.org/adding-elements-array-every-element-becomes-greater-k/

def main():
     nums = [1, 10, 12, 9, 2, 3]
     k = 10
     print num_operations_add_until_k(nums, k)

def num_operations_add_until_k(nums, k):
   q = Q.PriorityQueue()
   num_operations = 0
   for num in nums:
       q.put(num)

   while (1):

         min = q.get()
         if (min >= k):
            q.put(min)
            break
   
         #If the heap has only one element which is less than k
         if q.empty():
            return -1

         next_min = q.get()
         num_operations = num_operations + 1
         temp = min+next_min
         q.put(temp)

   return num_operations

main()
