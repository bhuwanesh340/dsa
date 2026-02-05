# Definition of singly linked list
class ListNode:
    def __init__(self, x=0, next=None):
        self.data = x
        self.next = next

class Solution:
    # Function to insert a new node before the given node
    def insertBeforeX(self, head, X, val):
        if head is None:
            return None
        
        # Insert at the beginning if 
        # the value matches the head's data
        if head.data == X:
            return ListNode(val, head)
        
        temp = head
        while temp.next is not None:
            # Insert at the current position if 
            # the next node has the desired value
            if temp.next.data == X:
                newNode = ListNode(val, temp.next)
                temp.next = newNode
                break
            temp = temp.next
        
        return head

# Helper Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    # Create a linked list from a list
    arr = [1, 2, 4, 5]
    X = 4
    val = 3
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])

    # Print the original list
    print("Original List: ", end="")
    printLL(head)

    # Create a Solution object
    sol = Solution()
    head = sol.insertBeforeX(head, X, val)

    # Print the modified linked list
    print("List after inserting a new node before the given node: ", end="")
    printLL(head)