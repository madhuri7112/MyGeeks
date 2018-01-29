import java.util.*;

public class FirstDuplicate {

  public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      String str = sc.nextLine();
      
      char firstDuplicate = findFirstDuplicate(str.toCharArray());

      System.out.println(firstDuplicate);
  }

  public static char findFirstDuplicate(char[] str) {
    HashMap<Character, Integer> frequency = new HashMap<Character, Integer>();

    for (int i = 0; i<str.length; i++) {
         if (!frequency.containsKey(str[i])) {
               frequency.put(str[i], 1);
         } else {
  System.out.println("uefwufg");
               //System.out.println(i);
               int f = frequency.get(str[i]);
               frequency.put(str[i], f+1);
         }
    }
   
    

    for(int i = 0; i<str.length; i++) {
        System.out.println(str[i]);
        System.out.println(frequency.get(str[i]));
        if (frequency.get(str[i])>1) {
            return str[i];
        }
    }

    return '\0';
  }

}
