def main():
   init_str = "aba"
   target = "aba"
   k = 9
   if (append_and_delete(init_str, target, k)):
      print "Yes"
   else:
      print "No"

def append_and_delete(init_str, target, k):
   init_l = len(init_str)
   target_l = len(target)

   if k > init_l + target_l:
     return True
   
   #find num of common characters from start
   common_chars = 0
   for index, ch in enumerate(init_str):

       if index >= target_l:
          break
       if ch == target[index]:
          common_chars = common_chars+1
       else:
          break

   min_num_operations = (init_l - common_chars) + (target_l - common_chars)
   
   if k < min_num_operations:
      return False
   elif k == min_num_operations:
      return True
   else:
     if (k-min_num_operations)%2 == 0:
       return True
     else:
       return False

main() 
