# Node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to delete the tail node of linked list
    def deleteTail(self, head):
        
        # If the list is empty or has only one node
        if head is None or head.next is None:
            return None  # Return None
        
        # Temporary pointer
        temp = head
        
        '''Traverse to the second last 
        node in the list'''
        while temp.next.next is not None:
            temp = temp.next
        
        # Delete the last node
        temp.next = None
        
        # Return head of modified list
        return head

# Helper Function to print the linked list
def printList(head):
    current = head
    while current:
        print(current.val, end=" ")
        current = current.next
    print()

# Helper Function to insert a new node at 
# the beginning of the linked list
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

    print("Original list: ")
    printList(head)

    # Creating an instance of Solution class
    sol = Solution()

    # Function call to delete the tail node
    head = sol.deleteTail(head)

    print("List after deleting tail: ")
    printList(head)