public class checkBST {


	public static void main(String args[]) {

	}


	public static void isBST(Node head, int min, int max) {

		  if (head == null) {
		  	return true;
		  }
          if (head.data >=max || head.data <= min) {
          	return false;
          }
          

          return isBST(head.right, head.data, max) && isBST(head.left, min, head.data);

	}
}