class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(20)
node2 = Node(25)
node3 = Node(0)
node4 = Node(10)
node5 = Node(27)
node6 = Node(30)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6

cur = node1
while cur:
    print(f"{cur.data} -> ", end="")
    cur = cur.next
print("None")

# -----------------------------------------------------------------------

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    
    head = Node(values[0])  # Create the head node
    current = head
    
    for value in values[1:]:
        new_node = Node(value)
        current.next = new_node  # Link the current node to the new node
        current = new_node  # Move to the new node
    
    return head

# Function to print the linked list
def print_linked_list(head):
    cur = head
    while cur:
        print(f"{cur.data} -> ", end="")
        cur = cur.next
    print("None")

# Example usage
values = [20, 25, 0, 10, 27, 30]  # Can be any list of values
head = create_linked_list(values)
print_linked_list(head)


# 50 operations that can be performed on a Linked List

# ### Basic Operations:
# 1. **Insert at the beginning**: Insert a new node at the start of the list.

# Function to insert a new node at the beginning of the linked list
def insert_at_beginning(head, new_data):
    new_node = Node(new_data)  # Create the new node
    new_node.next = head  # Point the new node's next to the current head
    head = new_node  # Make the new node the new head
    return head


# Insert a new node at the beginning
new_data = 150
head = insert_at_beginning(head, new_data)
print(f"\nLinked List after inserting {new_data} at the beginning:")
print_linked_list(head)

# 2. **Insert at the end**: Insert a new node at the end of the list.

# Function to insert a new node at the end of the linked list
def insert_at_end(head, new_data):
    new_node = Node(new_data)  # Create the new node
    
    # If the list is empty, the new node becomes the head
    if head is None:
        head = new_node
        return head
    
    # Traverse the list to find the last node
    current = head
    while current.next:
        current = current.next
    
    # Link the last node to the new node
    current.next = new_node
    return head


# Insert a new node at the end
new_data = 35
head = insert_at_end(head, new_data)
print(f"\nLinked List after inserting {new_data} at the end:")
print_linked_list(head)

# 3. **Insert at a specific position**: Insert a new node at a given position in the list.
# 4. **Delete the first node**: Remove the first node (head) of the list.
# 5. **Delete the last node**: Remove the last node (tail) of the list.
# 6. **Delete by value**: Remove the first node that contains the given value.
# 7. **Search for a value**: Check if a node with a specific value exists in the list.
# 8. **Get the length**: Count the number of nodes in the linked list.
# 9. **Print the list**: Traverse the linked list and print its elements.
# 10. **Clear the list**: Remove all nodes from the list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None
    
    head = Node(values[0])  # Create the head node
    current = head
    
    for value in values[1:]:
        new_node = Node(value)
        current.next = new_node  # Link the current node to the new node
        current = new_node  # Move to the new node
    
    return head

# Function to insert a new node at a specific position
def insert_at_position(head, new_data, position):
    new_node = Node(new_data)
    
    # If inserting at the beginning (position 0)
    if position == 0:
        new_node.next = head
        head = new_node
        return head
    
    current = head
    count = 0
    
    # Traverse the list until the position is reached
    while current and count < position - 1:
        current = current.next
        count += 1
    
    # If position is valid (not out of bounds)
    if current:
        new_node.next = current.next
        current.next = new_node
    else:
        print(f"Position {position} is out of bounds.")
    
    return head

# Function to delete the first node
def delete_first_node(head):
    if head:
        head = head.next
    return head

# Function to delete the last node
def delete_last_node(head):
    if not head or not head.next:  # If the list has only one node or is empty
        return None
    
    current = head
    while current.next and current.next.next:
        current = current.next
    
    current.next = None
    return head

# Function to delete a node by value
def delete_by_value(head, value):
    if not head:
        return None
    
    # If the head node itself contains the value
    if head.data == value:
        return head.next
    
    current = head
    while current.next and current.next.data != value:
        current = current.next
    
    if current.next:
        current.next = current.next.next  # Bypass the node containing the value
    else:
        print(f"Value {value} not found in the list.")
    
    return head

# Function to search for a value in the list
def search_for_value(head, value):
    current = head
    while current:
        if current.data == value:
            return True
        current = current.next
    return False

# Function to get the length of the linked list
def get_length(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

# Function to print the linked list
def print_linked_list(head):
    cur = head
    while cur:
        print(f"{cur.data} -> ", end="")
        cur = cur.next
    print("None")

# Function to clear the linked list
def clear_list():
    return None

# Example usage
values = [20, 25, 0, 10, 27, 30]  # Initial list of values
head = create_linked_list(values)

print("Original Linked List:")
print_linked_list(head)

# Insert at specific position
new_data = 15
position = 2
head = insert_at_position(head, new_data, position)
print(f"\nLinked List after inserting {new_data} at position {position}:")
print_linked_list(head)

# Delete the first node
head = delete_first_node(head)
print("\nLinked List after deleting the first node:")
print_linked_list(head)

# Delete the last node
head = delete_last_node(head)
print("\nLinked List after deleting the last node:")
print_linked_list(head)

# Delete by value
value_to_delete = 10
head = delete_by_value(head, value_to_delete)
print(f"\nLinked List after deleting the value {value_to_delete}:")
print_linked_list(head)

# Search for a value
value_to_search = 27
found = search_for_value(head, value_to_search)
print(f"\nSearching for value {value_to_search}: {'Found' if found else 'Not found'}")

# Get the length of the linked list
length = get_length(head)
print(f"\nLength of the linked list: {length}")

# Clear the linked list
head = clear_list()
print("\nLinked List after clearing:")
print_linked_list(head)












# ### Advanced Operations:
# 11. **Reverse the list**: Reverse the order of nodes in the list.
# 12. **Find the middle node**: Find the middle node of the list.
# 13. **Detect a loop**: Detect if the linked list contains a cycle (loop).
# 14. **Remove duplicates**: Remove duplicate values from the linked list.
# 15. **Merge two sorted lists**: Merge two sorted linked lists into a single sorted list.
# 16. **Find the intersection point of two lists**: Find where two linked lists intersect.
# 17. **Get the nth node from the end**: Return the nth node from the end of the list.
# 18. **Sort the list**: Sort the linked list elements.
# 19. **Swap nodes without swapping data**: Swap two nodes in the list without changing their data.
# 20. **Flatten a linked list**: Convert a multi-level linked list into a single-level list.
  
# ### Utility Operations:
# 21. **Check if the list is empty**: Check whether the linked list is empty.
# 22. **Create a new list from another list**: Create a new linked list by copying another list.
# 23. **Clone the list**: Create a deep copy of the entire linked list.
# 24. **Count occurrences of a value**: Count how many times a specific value appears in the list.
# 25. **Convert a linked list to an array**: Convert a linked list into a Python list (array).
# 26. **Convert an array to a linked list**: Convert a Python list (array) into a linked list.
# 27. **Get the tail node**: Retrieve the last node of the list.
# 28. **Check if a node exists**: Check if a particular node exists in the list by reference.
# 29. **Insert after a specific node**: Insert a node after a given node.
# 30. **Insert before a specific node**: Insert a node before a given node.
  
# ### Deletion Operations:
# 31. **Delete the node at a given index**: Remove the node at a specific index.
# 32. **Delete all nodes with a given value**: Remove all nodes containing a specific value.
# 33. **Delete a node using the node pointer**: Given a pointer to a node, delete that node.
# 34. **Delete a node by index**: Delete a node at a specific index in the list.
# 35. **Delete a node by position from the end**: Delete the node that is a certain number of positions from the end.

# ### Special Operations:
# 36. **Rotate the list**: Rotate the linked list by a given number of places.
# 37. **Flatten and sort the list**: Flatten and sort a multi-level linked list.
# 38. **Reverse a section of the list**: Reverse a section of the list between two positions.
# 39. **Remove the node with the maximum value**: Delete the node containing the highest value.
# 40. **Remove the node with the minimum value**: Delete the node containing the lowest value.

# ### Performance Optimizations:
# 41. **Find the kth largest element**: Find the kth largest node value in the list.
# 42. **Find the kth smallest element**: Find the kth smallest node value in the list.
# 43. **Detect if two lists are identical**: Check if two linked lists have the same structure and values.
# 44. **Check if a list is a palindrome**: Check if the linked list reads the same forward and backward.
# 45. **Merge k sorted lists**: Merge `k` sorted linked lists into one sorted list.

# ### Pointer Manipulation:
# 46. **Reverse the nodes in pairs**: Reverse every two consecutive nodes in the list.
# 47. **Partition list around a value**: Partition the list into two sublists, where one has elements less than a given value and the other has greater elements.
# 48. **Rotate the list left by k nodes**: Rotate the list by moving the first `k` nodes to the end.
# 49. **Cycle through the list**: Traverse the list in a cyclic manner (loop through without termination).
# 50. **Check if the list is circular**: Check if the linked list is circular (i.e., the last node points back to the head).

# ### More Details on Selected Operations:

# 1. **Reverse the list**: Can be done by reversing the `next` pointers of each node.
# 2. **Merge two sorted lists**: Use a two-pointer approach to merge them while maintaining order.
# 3. **Detect a loop**: Use Floyd's cycle-finding algorithm (Tortoise and Hare) to detect a cycle in linear time.
# 4. **Find the middle node**: Use two pointers, one moving 1 step at a time, the other 2 steps. When the faster pointer reaches the end, the slower pointer will be at the middle.
# 5. **Flatten a linked list**: Used for complex structures where each node contains a sublist. Flatten it into a single list.

