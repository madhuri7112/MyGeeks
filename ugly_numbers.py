

def main():
    print find_nth_ugly_number(150)

def find_nth_ugly_number(n):
    ugly_numbers = [1]
    
    mul_2_index = 0
    mul_3_index = 0
    mul_5_index = 0
    count = 1
    
    while (count<=n):
         next_ugly_number = min([ugly_numbers[mul_2_index]*2, ugly_numbers[mul_3_index]*3, ugly_numbers[mul_5_index]*5])
         ugly_numbers.append(next_ugly_number)
         if (next_ugly_number == ugly_numbers[mul_2_index]*2):
            mul_2_index = mul_2_index + 1 
         if (next_ugly_number == ugly_numbers[mul_3_index]*3):
           mul_3_index = mul_3_index + 1
         if (next_ugly_number == ugly_numbers[mul_5_index]*5): 
           mul_5_index = mul_5_index + 1
         

         count = count+1
    print ugly_numbers 
    return ugly_numbers[n-1]

main()   
