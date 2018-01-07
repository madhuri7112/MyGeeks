class LongestSpanBinaryArray {
	public static void main(String[] args) {
        int[] arr1 = {0, 0, 1, 0};
        int[] arr2 = {1, 1, 1, 1};

        int l = longestSpanMethod2(arr1, arr2);
        System.out.println(l);
	}

	public static int longestSpan(int[] list1, int[] list2) {
		  int length = list1.length;
          int totalSum1 = findSumOfList(list1);
          int totalSum2 = findSumOfList(list2);

          if (totalSum1 == totalSum2) {
          	return length;
          }
 
          int maxSpan = 0;
          int startPointer = 0;
          int endPointer = -1;
          int sum1 = 0;
          int sum2 = 0;

          int maxf = 0;
          int maxs = 0;

          int minSum = min(totalSum1, totalSum2);
          while(true) {
              if (sum1 > totalSum2 || sum2 > totalSum1) {
              	sum1 = sum1 - list1[startPointer];
              	sum2 = sum2 - list2[startPointer];
              	startPointer ++ ;
              } else if (endPointer<length-1) {
              	endPointer ++;
              	sum1 = sum1 + list1[endPointer];
              	sum2 = sum2 + list2[endPointer];
              	
              } else {
              	break;
              }
              if (sum1 == sum2 && (endPointer - startPointer +1) > maxSpan) {
                       maxSpan = endPointer - startPointer + 1;
                       maxf = endPointer;
                       maxs = startPointer;
              }
          }

          return maxSpan;
	}


    /**
     *  LongestSpan2 method -- subtract list1 from list2
     *  Then find the longest span with sum 0(Keep in mind that this array has -ve numbers as well)
     *
     * @param Array list1 - 1st list
     * @param Array list2 - 2nd list
     */
	public static int longestSpanMethod2(int[] list1, int[] list2)
	{
		int n = list1.length;
		System.out.println(n);
        int[] diffArray = new int[n];

        for (int i=0; i<n; i++) {
        	diffArray[i] = list1[i] - list2[i];
        }

        /*FInding max span with sum 0 in diffarray*/
        /*Computing sum array for diffarray*/

        int[] diffSumArray = new int[n];

        diffSumArray[0] = diffArray[0];

        for (int i=1; i<n; i++) {
        	diffSumArray[i] = diffSumArray[i-1] + diffArray[i];
        }

        printArray(diffSumArray);
        /*We need to find two indices whose value is same and are at max distance in this diffSumArray*/
        /*The possible values for diffsum array is - n to n...so maintain a hashmap for this differnces*/

        int[] hMap = new int[2*n+1];
        for (int i=0;i<2*n +1;i++) {
        	hMap[i] = -1;
        }

        int maxSpan = 0;
//-1 -1 -2 -3   n = 4
        for (int i=0;i<n;i++) {
        	int diff = diffSumArray[i];
        	int hashIndex = diff + n;
            
            if (diff == 0) {
                maxSpan = i+1;
            } else if (hMap[hashIndex] == -1) {
        		hMap[hashIndex] = i;
        	} else {
               if (i - hMap[hashIndex]  > maxSpan) {
               	   maxSpan = i - hMap[hashIndex] ;
               }
        	}
        	System.out.println(maxSpan);
        }

        return maxSpan;
	}


    public static void  printArray(int[] ls)
    {
         int n = ls.length;
         System.out.println(n);
         System.out.println("*********");
         for(int i=0;i<n;i++) {
         	System.out.print(ls[i]);
         	System.out.print("  ");
         }
         System.out.println("*********");
    }
    
    public static int min(int i1, int i2) {
    	if (i1<i2) {
    		return i1;
    	} else {
    		return i2;
    	}
    }

	public static int findSumOfList(int[] list) {
        int sum = 0;
        for(int i=0; i<list.length; i++) {
           sum = sum + list[i];
        }

        return sum;
	}
}