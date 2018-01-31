#https://www.hackerrank.com/contests/crescent-practice-3rd-years/challenges/add-them-up/problem
# Enter your code here. Read input from STDIN. Print output to STDOUT
def main():
    
    num_tc = input()
    for tc in range(num_tc):
        print "Case "+str(tc+1)+":"
        len = input()
        inp = map(int, raw_input().strip().split(' '))
        sum_array = compute_sum_array(inp)
        num_queries = input()
        for q in range(num_queries):
            query_params = map(int, raw_input().strip().split(' '))
            start = query_params[0]
            end = query_params[1]
                   
            if start == 1:
                print str(sum_array[end-1])
            else:
                print str(sum_array[end-1] - sum_array[start-2])

def compute_sum_array(inp):
    sum_array = []
    sum = 0
    
    for num in inp:
        sum = sum + num
        sum_array.append(sum)
    #print sum_array   
    return sum_array

main()
    
