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

    return head

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
         if temp == head:
             head = head.next_node 
         else:
             temp_prev.next_node = temp.next_node
             temp.next_node = None

     return head

def delete_middle_of_ll(head):
    
    slow_ptr = head
    fast_ptr = head
    slow_prev_ptr = head

    while (fast_ptr.next_node and fast_ptr.next_node.next_node):
        slow_prev_ptr = slow_ptr
        slow_ptr = slow_ptr.next_node
        fast_ptr = fast_ptr.next_node.next_node
   
    if (not head.next_node):
       head = None
    elif (not head.next_node.next_node):
       temp = head
       head = head.next_node
       temp.next_node = None
    else:
       slow_prev_ptr.next_node = slow_ptr.next_node
       slow_ptr.next_node = None

    return head




def test_ll_operations():
     head = create_head_node(1)
     head = add_element(head, 2)
     head = delete_middle_of_ll(head)
     print_list(head)
     return
     head = add_element(head, 3)
     head = add_element(head, 4)
     head = add_element(head, 5)
    #head = remove_element(head, 2)
     head = add_element(head, 6)
     head = add_element(head, 7)
    # head = add_element(head, 8)
    #head = remove_element(head, 6)
    #head = remove_element(head, 1)
     head = delete_middle_of_ll(head)
     print_list(head)
 
def main():
    test_ll_operations()

main()

