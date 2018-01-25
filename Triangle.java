import java.util.*;

class Triangle {

   public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       int tc = sc.nextInt();
 
       for (int i=0;i<tc;i++) {
          int side_a = sc.nextInt();
          int side_b = sc.nextInt();
          int side_c = sc.nextInt();

          checkForTriangle(side_a, side_b, side_c);
       }
   } 


   public static  void checkForTriangle(int side_a, int side_b, int side_c) {
        if (
            !(side_a + side_b > side_c) ||
            !(side_b+side_c > side_a) ||
            !(side_c+side_a > side_b)
            ) {
           
           System.out.println("NOT VALID");
           return;
        }

        if (side_a == side_b && side_b == side_c) {
           System.out.println("EQUILATERAL");
           return;
        }
 
        if (side_a == side_b || side_b == side_c || side_c == side_a) {
          System.out.println("ISOSCLES");
          return;
        }
    
        System.out.println("SCALAR");

        return;
   }

}
