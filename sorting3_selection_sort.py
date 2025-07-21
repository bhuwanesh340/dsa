def selection_sort(arr):
    for pos in range(len(arr)-1):
        # current = arr[pos]
        min_pos = pos

        for j in range(pos, len(arr)):
            if arr[j] < arr[min_pos]:
                min_pos = j

        # swap
        temp = arr[pos]
        arr[pos] = arr[min_pos]
        arr[min_pos] = temp

    return arr


arr = [3,2,1,5,4]

sorted = selection_sort(arr)
print(sorted)
        