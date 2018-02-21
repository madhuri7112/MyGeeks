import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

class Stack {
    int[] nums;
    int size;
    int top;
    
    public Stack(int size) {
        this.size = size;
        nums = new int[size];
        top = -1;
    }
    
    public void push(int n) {
        top = top + 1;
        nums[top] = n;
    }
    
    public int pop() {
        int topElement = nums[top];
        top = top -1;
        
        return topElement;
    }
    
    public int top() {
        int topElement = nums[top];
        
        return topElement;
    }
    
    public boolean empty() {
        return (top == -1);
    }
}

public class NextGreatestElement {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        int[] inp = {2,7,3,4,5,13,9};
        printNextGreaterElement(inp);
    }
    
    public static void printNextGreaterElement(int[] inp) {
        int size = inp.length;
        Stack st = new Stack(size);
        if (size == 1) {
            System.out.printf("%d %d",inp[0],-1);
            return;
        }
        
        int current_index = 1;
        st.push(inp[0]);
        while (current_index<size) {
            int current_element = inp[current_index];
            
            while (!st.empty() && current_element>st.top()) {
                System.out.printf("%d %d \n",st.top(), current_element);
                st.pop();
            }
            
            st.push(current_element);
            current_index = current_index +1;
        }
        
    }
}
//2,7,3,4,5,13,9
