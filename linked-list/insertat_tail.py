class ListNone:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertAtTail(self, head, val):
        new_node = ListNone(val)
        if not head:
            return new_node
        
        current = head
        while current.next != None:
            current = current.next

        current.next = new_node
        
        return head
    
def printLL(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
sol = Solution()
head = None
head = sol.insertAtTail(head, 1)
head = sol.insertAtTail(head, 2)
head = sol.insertAtTail(head, 3)
printLL(head)  # Output: 1 -> 2 -> 3 -> None

