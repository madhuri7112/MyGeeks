#https://www.geeksforgeeks.org/print-possible-strings-can-made-placing-spaces/

def print_with_spaces(str, buffer_string, current_index):
    
      if(current_index == len(str)):
        print buffer_string
        return 
      #print current_index
      buffer_string = buffer_string + str[current_index]
      current_index = current_index +1
      print_with_spaces(str, buffer_string, current_index)

      if current_index!=1:
        buffer_string = buffer_string[:-1] + " " + buffer_string[len(buffer_string) - 1]
        print_with_spaces(str, buffer_string, current_index)
     
def main():

     print_with_spaces("abcd", "", 0)
   
main()
      
      

  
