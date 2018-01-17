#https://www.geeksforgeeks.org/find-lost-element-from-a-duplicated-array/
#This solution is assuming the two arrays are sorted
def main():
  orig = [1, 4 ,5, 7, 9, 16]
  missing = [1,5,7,9,16]
  num = find_lost_element(orig, missing)
  print num
 
#first is the original array and second is the one with missing element
def find_lost_element(orig_list, missing_list):
     l = len(orig_list)
     if (l == 2):
        if (orig_list[0] == missing_list[0]):
            return orig_list[1]
        else:
           return orig_list[0]

     if (orig_list[l/2] == missing_list[l/2]):
         return find_lost_element(orig_list[l/2:], missing_list[l/2:])
     else:
         return find_lost_element(orig_list[:l/2+1], missing_list[:l/2+1])
     
main()     
