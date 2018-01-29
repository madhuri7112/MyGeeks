import java.util.*;
import java.lang.*;


public class MinGates {

   public static void main(String args[]) {
          Scanner sc = new Scanner(System.in);
 
          int num_tc = sc.nextInt();
          while (num_tc !=0) {
               int num_flights = sc.nextInt();
               int[] arr = new int[num_flights];
               int[] dep = new int[num_flights];
               for (int i=0; i<num_flights;i++) {
                   arr[i] = sc.nextInt();
               }
               for (int i=0; i<num_flights;i++) {
                   dep[i] = sc.nextInt();
               }
               System.out.println(findMinGatesNeeded(arr, dep));
               num_tc --;
          }
   }

   public static int findMinGatesNeeded(int[] arr, int[] deps) {


       
       int numGates = 0;
       int maxGates = 0;
       PriorityQueue<Integer> endTimeQueue = new PriorityQueue<Integer>();
       for (int i=0;i<arr.length;i++) {
             int arrTime = arr[i];
             Integer earliest_end_time = endTimeQueue.peek();
             if (earliest_end_time == null) {
                   if (numGates == 0) {
                     numGates = numGates + 1;
                   }
             } else {
                 if (earliest_end_time <= arrTime) {
                        //Remove this endtime
                        endTimeQueue.poll();
                 } else {
                         numGates ++;
                 }
             }
             endTimeQueue.add(deps[i]);
             maxGates = Math.max(maxGates, numGates);
       }
       return maxGates;
   }
}
