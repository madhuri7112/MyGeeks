class Node:
  def __init__(self, data):
     self.data = data
     self.next_node = None


def create_head_node(data):

     head = Node(data)
     
     return head

def add_element(head, new_data):
  
    new_node = Node(new_data)
    temp = head
    while(temp.next_node):
        temp = temp.next_node

    temp.next_node = new_node

def print_list(head):

    temp = head
    while (temp):
       print temp.data
       temp = temp.next_node
    
    return

def remove_element(head, target_data):

     temp = head
     temp_prev = head
     target_element = None

     while(temp):
         if (temp.data == target_data):
               target_element = temp
               break
         temp_prev = temp
         temp = temp.next_node

     if (target_element):
         temp_prev.next_node = temp.next_node
         temp.next_node = None

     return

def test_ll_operations():
     head = create_head_node(1)
     add_element(head, 2)
     add_element(head, 3)
     add_element(head, 4)
     remove_element(head, 2)
     add_element(head, 6)
     add_element(head, 7)
     remove_element(head, 6)
     print_list(head)
 
def main():
    test_ll_operations()

main()

