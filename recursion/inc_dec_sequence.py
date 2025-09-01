def decreasing(n):
    if n == 0:
        return
    print(n, end=" ")
    decreasing(n-1)

num = 5
decreasing(num)
print()

def increasing(n):
    if n == 0:
        return
    increasing(n-1)
    print(n, end=" ")

num = 10
increasing(num)