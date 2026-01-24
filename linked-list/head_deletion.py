# Node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to delete the head node of the linked list
    def deleteHead(self, head):
        # If list is empty, nothing to delete
        if head is None:
            return None
        
        # Set temporary pointer
        temp = head
        
        # Update head to the next node 
        head = head.next
        
        # Delete original head    
        del temp
        
        # Return new head          
        return head

# Function to print the linked list
def printList(head):
    current = head
    while current is not None:
        print(current.val, end=" ")
        current = current.next
    print()

# Function to insert a new node at the beginning of the linked list
def insertAtHead(head, data):
    newNode = ListNode(data)
    newNode.next = head
    head = newNode
    return head

if __name__ == "__main__":
    # Create a linked list
    head = None
    head = insertAtHead(head, 3)
    head = insertAtHead(head, 2)
    head = insertAtHead(head, 1)

    print("Original list: ", end="")
    printList(head)
    
    # Creating an instance of Solution Class
    sol = Solution()
    
    # Function call to delete the head node
    head = sol.deleteHead(head)

    print("List after deleting head: ", end="")
    printList(head)