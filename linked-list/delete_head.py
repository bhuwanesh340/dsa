'''
Given the head of a singly linked list, delete the head of the linked list and 
return the head of the modified list. The head is the first node of the linked list.
'''

# Node structure
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteHead(self, head):
        head = head.next
        return head
    
def printLinkedList(head):
    current = head
    while current is not None:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# example usage:
def insertAtHead(head, data):
    newNode = ListNode(data)
    newNode.next = head
    head = newNode
    return head


if __name__ == "__main__":
    head = None
    head = insertAtHead(head, 3)
    head = insertAtHead(head, 2)
    head = insertAtHead(head, 1)

    print("Original list: ")
    printLinkedList(head)

    sol = Solution()
    head = sol.deleteHead(head)

    print("List after deleting head: ")
    printLinkedList(head)