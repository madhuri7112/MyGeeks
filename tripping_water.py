def main():
    heights = [2, 0, 2]
    vol = calculate_volume_m1(heights)

    print vol

#This method computes the max left and max right element for each element
def calculate_volume_m1(heights):
      max_right = {}
      max_left = {}
      num = len(heights)
      max_ht = 0
      #Calculating max left
      for index, ht in enumerate(heights):
        if ht>max_ht:
          max_ht = ht

        max_left[index] = max_ht
      max_left[0] = 0

      #Computing max right array 
      max_ht = 0 
      for index, ht in reversed(list(enumerate(heights))):
          if ht>max_ht:
            max_ht = ht
          max_right[index] = max_ht

      max_right[num -1] = 0
      
      volume = 0 
      for index in range(num):
          volume = volume + max((min(max_left.get(index), max_right.get(index)) - heights[index]),0)

      return volume

#This method does not use extra O(n) space
def calculate_volume_m2(heights):

     max = 0 
     vol = 0
     for index, ht in enumerate(heights):
         
    
main()       
