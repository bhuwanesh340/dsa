# Node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteKthNode(self, head, k):
      """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
      """
      if k == 1:
        temp = head
        head = head.next
        del temp
        return head

      cnt = 0
      prev = None
      temp = head
      while temp != None:
        cnt += 1
        if cnt == k:
          prev.next = prev.next.next

        prev = temp
        temp = temp.next

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
    head = insertAtHead(head, 5)
    head = insertAtHead(head, 4)
    head = insertAtHead(head, 3)
    head = insertAtHead(head, 2)
    head = insertAtHead(head, 1)

    print("Original list: ")
    printList(head)

    # Creating an instance of Solution class
    sol = Solution()

    k = 3
    # Function call to delete the k-th node
    head = sol.deleteKthNode(head, k)
    print("After deleting the 3rd node: ")
    printList(head)