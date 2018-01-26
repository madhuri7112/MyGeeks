import Queue as Q

def main():
    arr = [56, 21, 42, 67, 23, 74]
    print (get_largest_derangement(arr))

def get_largest_derangement(arr):
    q = Q.PriorityQueue()
    dearr = []
    n = len(arr)
    for num in arr:
       q.put((-1*num, num))
    i = 0 
    while not q.empty():
      max_num = q.get()
      print max_num
      if (max_num != arr[i] or i==n-1):
          dearr.append(max_num[1])
      else:
          sec_max_num = q.get()
          #print max_num
          #print sec_max_num
          dearr.append(sec_max_num[1])
          q.put(max_num)
      i = i+1

    return dearr

main()
