public class Rearrange {
	public static void main(String args[]) {
       int[] arr = {1,3,0,2};
       rearrange(arr);
	}

	public static void rearrange(int[] arr) {
        int currentIndex = 0;
        int currentIndexValue = arr[0];

        /*To make all the values positive*/
        for(int i=0; i< arr.length; i++) {
        	arr[i] = arr[i]+1;
        }

        for (int i=0; i<arr.length; i++) {
        	if (arr[i] > 0) {
        	  reaarrangeCycle(arr, i);	
        	}
        	
        }

        for(int i=0; i< arr.length; i++) {
        	arr[i] = -1*arr[i]-1;
        	System.out.println(arr[i]);
        }

	}

	public static void reaarrangeCycle(int[] arr, int startIndex) {
        
        int index = startIndex;
        int value = arr[startIndex] - 1;
        
        do {
            
            int temp = arr[value];
            arr[value] = -1 * (index + 1);

            index = value;
            value = temp - 1;
            
            
        } while (index!=startIndex);
	}
}