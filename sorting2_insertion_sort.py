def insertion_sort(arr):
    for i in range(1, len(arr)):
        # take the current element
        current = arr[i]

        # get previous index
        prev = i-1

        # loop until index becomes -1 and previous number > current number (for swapping)
        while (prev>=0 and arr[prev] > current):
            # swap the next element with previous
            arr[prev+1] = arr[prev]

            # go back to previous element
            prev -= 1

        # replace the last index with current value
        arr[prev+1] = current

        print(arr)
        print("***********")

    return arr


arr = [5,3,2,1,6]

sorted = insertion_sort(arr)
print(sorted)