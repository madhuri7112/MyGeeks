

class Stack {
      int[] data;
      int size;
      int top;

      public void stack(int size) {
         data = new int[size];
         top = -1;
      }

     public int push(int n) {
         top ++;
         data[top] = n;
     }

     public void pop() {

         if (top == -1) {
             return;
         }
         data[top] = 0;
         top --;
     }

     public int top() {
         if (top == -1) {
             return -1;
         } 

         return data[top];   
     }
     
}


public class LMaxStack
{
  public static void main(String[] args) {
    
  }
}
