# Definition of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to insert at head
    def insertAtHead(self, head, X):
        # Creating a new node
        newnode = ListNode(X)
        
        ''' Making next of newly created node to 
        point to the head of the LinkedList '''
        newnode.next = head
        
        # Making newly created node as head
        head = newnode
        
        # Return the head of modified list
        return head

# Helper Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    # Create a linked list from a list
    arr = [20, 30, 40]
    X= 10
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])

    # Print the original list
    print("Original List: ", end="")
    printLL(head)

    # Create a Solution object
    sol = Solution()
    head = sol.insertAtHead(head, X)

    # Print the modified linked list
    print("List after inserting the given value at head: ", end="")
    printLL(head)