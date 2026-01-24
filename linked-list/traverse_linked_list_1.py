class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data, end=" -> ")
        current = current.next

    print("None")

# Example usage:
# Creating a linked list: 1 -> 2 -> 3 -> None
arr = [2,5,7,9]

y1 = Node(arr[0])
y2 = Node(arr[1])
y3 = Node(arr[2])
y4 = Node(arr[3])

y1.next = y2
y2.next = y3
y3.next = y4

print("Traversing the linked list:")
printLinkedList(y1)  # Output: 1 -> 2 -> 3 -> None