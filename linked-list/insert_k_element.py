# Definition of singly linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Function to insert a new node at the kth position 
    def insertAtKthPosition(self, head, X, K):
        ''' If the linked list is empty 
        and k is 1, insert the 
        new node as the head '''
        if head is None:
            if K == 1:
                return ListNode(X)
            else:
                return head
        
        ''' If K is 1, insert the new
        node at the beginning 
        of the linked list '''
        if K == 1:
            return ListNode(X, head)
        
        cnt = 0
        temp = head

        ''' Traverse the linked list 
        to find the node at position k-1 '''
        while temp is not None:
            cnt += 1
            if cnt == K - 1:
                ''' Insert the new node after the node 
                at position k-1 '''
                newNode = ListNode(X, temp.next)
                temp.next = newNode
                break
            temp = temp.next
        
        return head

# Helper Function to print the linked list
def printLL(head):
    while head is not None:
        print(head.val, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    # Create a linked list from a list
    arr = [10, 30, 40]
    X = 20
    K = 2
    head = ListNode(arr[0])
    head.next = ListNode(arr[1])
    head.next.next = ListNode(arr[2])

    # Print the original list
    print("Original List: ", end="")
    printLL(head)

    # Create a Solution object
    sol = Solution()
    head = sol.insertAtKthPosition(head, X, K)

    # Print the modified linked list
    print("List after inserting the given value at the Kth position: ", end="")
    printLL(head)