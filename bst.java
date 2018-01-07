

class Node {  
    Node leftChild;
    int data;
    Node rightChild;

    public Node(int data, Node leftChild, Node rightChild) {
    	this.leftChild = leftChild;
    	this.data = data;
    	this.rightChild = rightChild;
    }
}

class Stack {
	public int maxSize;
    public Node[] stack;
    public int top;

    public Stack(int maxSize) 
    {
       this.maxSize = maxSize;
       this.stack = new Node[maxSize];
       this.top = -1;
    }

    public void push(Node node)
    {
    	//System.out.println("Pushing.   " + node.data);
        top = top+1;
        this.stack[top] = node;
    }

    public Node pop()
    {
    	if (top == -1) {
    		return null;
    	}

        Node topElement = stack[top];
        //System.out.println("Popping.   " + topElement.data);
        top = top - 1;

        return topElement;
    }


    public void printStack() 
    {
    	for(int i = top; i>=0; i--) {
    		System.out.println(stack[i].data);
    	}
    }

    public void emptyStack()
    {
    	top = -1;
    }
}

class Queue {
	public int maxSize;
	public Node[] que;
	public int start;
	public int end;


    public queue(int maxSize)
    {
    	this.maxSize = maxSize;
        que = new Node[maxSize];
        start = 0;
        end = 0;
    }

	public void enque(Node node)
	{      
        que[end] = node;  
        end++;     
	}

	public void deque(Node node)
	{
		firstElement = que[start];
		start ++;

		return firstElement;
	}
}


public class bst {

    public static Stack pathStack = new Stack(100);


	public static void main(String args[]) {

         Node head = createBST(5);
         insertIntoBst(head, 7);
         insertIntoBst(head, 6);
         
         insertIntoBst(head, 2);
         insertIntoBst(head, 1);
         insertIntoBst(head, 21);
         insertIntoBst(head, 11);
         insertIntoBst(head, 14);
         insertIntoBst(head, 3);



         // int d = maxNumWR(head);
         // System.out.println(d);
         //printKDistanceNodes(head, 0, 4);

         // searchInTree(head, 11);
         // pathStack.printStack();
         // System.out.println("**************\n");
         // pathStack.emptyStack();
         // searchInTree(head, 1);
         // pathStack.printStack();

     
         // Node n = findLcaInBST(head,6,1);
         // System.out.println(n.data);
         // int n = maxDepthOfTree(head);
         // System.out.println(n);
	}

	public static Node findLCA(Node head, int n1, int n2) {

        if (head == null) {
        	return null;
        }
		if (head.data == n1 || head.data == n2) {
			return head;
		}

		Node leftLCA = findLCA(head.leftChild, n1, n2);
		Node rightLCA = findLCA(head.rightChild, n1, n2);

		if (rightLCA!= null && leftLCA != null) {
			return head;
		}

		if (leftLCA == null) {
			return rightLCA;
		} else {
			return leftLCA;
		}
	}

	

	public static Node createBST(int headData) {
          Node head = new Node(headData, null, null);
          //System.out.println(head.data);
          return head;
	}

    public static void insertIntoBst(Node head, int data) {
 
          Node newNode = new Node(data, null, null);
          while(true) {

          	   if (data > head.data) {
          	   	    if (head.rightChild == null) {
          	   	    	head.rightChild = newNode;
          	   	    	break;
          	   	    } else {
          	   	    	head = head.rightChild;
          	   	    }
          	   } else {
          	   	    if (head.leftChild == null) {
                        head.leftChild = newNode;
                        break;
          	   	    } else {
          	   	    	head = head.leftChild;
          	   	    }
          	   }
          }
    }

    // public static Node remove(Node head, int data) {

    // }
    
    public static Node searchInBst(Node head, int data) {

    	     while (head!= null) {

    	     	  if (head.data == data) {
    	     	  	 return head;
    	     	  } else if (data > head.data) {
                     head = head.rightChild;
    	     	  } else {
    	     	  	 head = head.leftChild;
    	     	  }
    	     }

    	     return null;
    }

    
    
    public static Node searchInTree(Node head, int data) 
    {

          if (head == null) {
          	return null;
          }

    	  pathStack.push(head);
          if (head.data == data) {
          	  return head;
          }
          
          if (head.rightChild !=null) {
          	  Node rel = searchInTree(head.rightChild, data);
              if (rel == null) {
              	pathStack.pop();
              } else {
              	return rel;
              }
          }
          
          if (head.leftChild !=null) {
              Node rel2 = searchInTree(head.leftChild, data);
              if (rel2 == null) {
              	 pathStack.pop();          	 
              } else {
              	return rel2;
              }
          }
          

          return null;

    }

    public static void printInOrder(Node head) 
    {
        if (head.leftChild != null) {
        	printInOrder(head.leftChild);
        }
        if (head != null) {
        	System.out.println(head.data);	
        }
        if (head.rightChild != null) {
        	printInOrder(head.rightChild);
        }
    }

    public static void printPreOrder(Node head)
    {
        if (head != null) {
           System.out.println(head.data);	
        }
        if (head.leftChild != null) {
        	printPreOrder(head.leftChild);
        }
        if (head.rightChild != null) {
        	printPreOrder(head.rightChild);
        }

    }

    public static void printPreOrderNonRecursive(Node head) 
    {
        
        Stack myStack = new Stack(100);

        while(true) {
        	while (head != null) {
               System.out.println(head.data);
               myStack.push(head);
               head = head.leftChild;
            }
            head = myStack.pop();
            if (head == null) {
            	return;
            }
            head = head.rightChild;
        }
    }


    public static void printInOrderNonRecursive(Node head)
    {
    	Stack myStack = new Stack(100);

    	while(true) {
    		while (head!=null) {
    			myStack.push(head);
    			head = head.leftChild;
    		}

            head = myStack.pop();

            if (head == null) {
            	return;
            }

    		System.out.println(head.data);
    		head = head.rightChild;

    	}
    }

    // public static void printPostOrderNonRecursive(Node head)
    // {
    // 	Stack myStack = new Stack(100);

    // 	while(true) {
    // 		while (head!=null) {
    // 			myStack.push(head);
    // 			head = head.leftChild;
    // 		}

    // 		head = myStack.pop();

    // 		while () {

    // 		}
    // 	}
    // }

    public static void printPostOrder(Node head)
    {
        if (head.leftChild != null) {
        	printInOrder(head.leftChild);
        }
        if (head.rightChild != null) {
        	printInOrder(head.rightChild);
        }
        if (head != null) {
           System.out.println(head.data);	
        }
        
    }

    public static Node printPath(Node head, int n)
    {
    	 if (head == null) {
    	 	return null;
    	 }
         if (head.data == n) {
         	System.out.println(head.data);
         	return head;
         }

         Node leftPath = printPath(head.leftChild, n);
         Node rightPath = printPath(head.rightChild, n);

         if (leftPath!=null || rightPath!=null) {
         	
         	 System.out.println(head.data);
         	 Node r = (leftPath!=null) ?  leftPath :  rightPath;
         	 return r;
         	}

         return null;

    }



    // public static void printBFS(Node head)
    // {
    // 	if(head == null) {
    // 		return;
    // 	}
    // 	System.out.println(head.data);
    // 	printBFS(head.leftChild);
    // 	printBFS(head.rightChild);

    // }

    // public static void printDFS(Node head)
    // {
    // 	if() {

    // 	}
    // }


    public static int depthOfNode(Node head, int n)
    {
    	if (head == null) {
    		return -1;
    	}

    	if (head.data == n) {
    		return 0;
    	}

    	int leftHeight = depthOfNode(head.leftChild, n);

    	if (leftHeight>=0) {
    		return leftHeight + 1;
    	}

    	int rightHeight = depthOfNode(head.rightChild, n);

    	if (rightHeight>=0) {
    		return rightHeight + 1;
    	}
        
        return -1;

    }

   
    
    public static int maxDepthOfTree(Node head)
    {
         if (head.leftChild == null && head.rightChild == null) {
         	return 0;
         }

         int leftHeight = 0;
         int rightHeight = 0;
         if (head.leftChild != null) {
              leftHeight = maxDepthOfTree(head.leftChild);
         }
         if (head.rightChild != null) {
         	rightHeight = maxDepthOfTree(head.rightChild);
         }

         return 1 + max(leftHeight, rightHeight);

    }

    public static int max(int n1, int n2) {
    	if (n1>=n2) {
    		return n1;
    	} else {
    		return n2;
    	}
    }

    public static boolean isLeaf(Node node)
    {
        if (node.leftChild == null && node.rightChild == null) {
        	return true;
        }

        return false;
    }

    public static void printRootToLeafPaths(Node head, Stack path)
    {
    	path.push(head);
    	if (isLeaf(head)) {
    		path.printStack();
    		System.out.println("*********\n");
    		return;
    	}

    	if (head.rightChild != null) {
    		printRootToLeafPaths(head.rightChild, path);
    		path.pop();
    	}

    	if (head.leftChild != null) {
    		printRootToLeafPaths(head.leftChild, path);
    		path.pop();
    	}
    }

    /**
     * Find LCA in binary search tree , assume n1 > n2
     */
    public static Node findLcaInBST(Node head, int n1, int n2)
    {
        if (head == null) {
              return null;
        }
        
        if (head.data == n1 || head.data == n2) {
        	return head;
        }

        if (n1>head.data && n2< head.data) {
               return head;
        }

        if (n1<head.data) {
        	return findLcaInBST(head.leftChild, n1, n2);
        }

        if (n2>head.data) {
        	return findLcaInBST(head.rightChild, n1, n2);
        }

        return null;
    }

    public static boolean isTreeSumTree(Node head)
    {
    	if (head == null || isLeaf(head)) {
    		return true;
    	}

    	int sumOfChildrenData = 0;
    	

        if (!isTreeSumTree(head.leftChild) || !isTreeSumTree(head.rightChild)) {
        	return false;
        }

        int ls = 0;
        int rs = 0;

        if (head.leftChild == null) {
        	ls = 0;
        } else if (isLeaf(head)) {
        	ls = head.data;
        } else {
        	ls = 2*head.data;
        }

        if (head.rightChild == null) {
        	rs = 0;
        } else if (isLeaf(head)) {
        	rs = head.data;
        } else {
        	rs = 2*head.data;
        }

        if (ls+rs == head.data) {
        	return true;
        } else {
        	return false;
        }
  	
    }

    public static void printKDistanceNodes(Node head, int currentDistance, int k)
    {
    	if (head == null) {
    		return;
    	}
        if (currentDistance == k) {
        	System.out.println(head.data);
        }

        currentDistance++;
        printKDistanceNodes(head.leftChild, currentDistance, k);
        printKDistanceNodes(head.rightChild, currentDistance, k);

        return;
    }

    public static int maxNumWR(Node head) 
    {
        Stack myStack = new Stack(100);

        int min = head.data;

        while (true) {
        	while(head != null) {
        	    myStack.push(head);
        	    if (head.data<min) {
        	    	min = head.data;
        	    }
        	    head = head.leftChild;
            }

            head = myStack.pop();
            if (head == null) {
            	break;
            }
            head = head.rightChild;
        }
        
        return min;
    }

    public static void printBFS(Node head)
    {
    	 Queue myQueue = new Queue(100);
         System.out.println(head.data);

         while (head != null) {
         	    if (head.leftChild!=null) {
         	       myQueue.enque(head.leftChild);
         	       System.out.println(head.leftChild.data);
                }
		        if (head.rightChild!=null) {
		           myQueue.enque(head.rightChild);
		           System.out.println(head.rightChild.data);
		        }

		        head = myQueue.deque();
         }
    }

    public static void correctSwappedNodes(Node head)
    {
    	
    }

}