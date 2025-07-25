arr = [10,20,30,40,50,60]
n = len(arr)


def printSubarray(arr, n):
    for i in range(0,n):
        for j in range(i,n):
            for k in range(i,j+1):
                print(arr[k], end=" ")
                print("k")
            print("j")

    return True

printSubarray(arr,n)