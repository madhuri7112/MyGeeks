import java.lang.*;

class CheckConsecutive {
 
    public static void main(String args[]) {
          int[] nums = {1,2,4,4,5};
          System.out.println(checkConsecutive(nums));
    }

    public static boolean checkConsecutive(int[] nums) {
        int l = nums.length;
        int max = nums[0];
        int min = nums[0];
  
        for (int i =0; i<l;i++) {
           if (nums[i] > max) {
               max = nums[i];
           }
 
           if (nums[i] < min) {
               min = nums[i];
           }
        }

        if (max - min + 1 != l) {
           return false;
        }

        for (int i=0;i<l;i++) {
            int num = nums[i];
 
            if ( nums[Math.abs(num) - min] < 0 ) {
                return false;
            }
 
            nums[Math.abs(num) - min] = -1 * nums[Math.abs(num) - min];
        } 

        for (int i =0;i<l;i++) {
            if (nums[i] > 0) {
              return false;
            }
        }
        
        return true;
    }

}
