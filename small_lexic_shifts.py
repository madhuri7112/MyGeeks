#https://www.geeksforgeeks.org/lexicographically-smallest-array-k-consecutive-swaps/

def main():
   input = [7, 6, 9, 2, 1, 3, 5, 2]
   max_shifts = 5
   find_smallest_lex_array(input, max_shifts)

def find_smallest_lex_array(input, max_shifts):
   
   shifts = 0

   #index of string which is being minimized
   pos = 0
   #7 6 9 2 1
   while(shifts<max_shifts and pos<len(input)):
      
       shifts_remaining = max_shifts - shifts
       min_index = pos
       for i in range(pos, pos+shifts_remaining+1):
            if (input[i] < input[min_index]):
                min_index = i
       
       min_element = input[min_index]
       pos_element = input[pos]
       #Shift the character till the min index element
       for i in range(min_index-1, pos-1, -1):
          input[i+1] = input[i]
       input[pos] = min_element
       shifts = shifts + (min_index - pos)
       pos = pos+1 
   print input
      
main() 

 
 
