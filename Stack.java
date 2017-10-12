public class Stack {
	public int maxSize;
    public int[] stack;
    public int top;

    public Stack(int maxSize) 
    {
       this.maxSize = maxSize;
       this.stack = new int[maxSize];
       this.top = -1;
    }

    public void push(int data)
    {
        top = top+1;
        this.stack[top] = data;
    }

    public int pop()
    {
        topElement = stack[top];
        top = top - 1;

        return topElement
    }
}