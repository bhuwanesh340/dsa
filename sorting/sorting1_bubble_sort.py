def bubble_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, len(arr)-i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp

            print(arr)

        print("**********")

    return arr

arr = [5,4,3,2,1]
sorted = bubble_sort(arr)

print(sorted)