# arr = [3,7,-4,1,2,1,-9,6]
# sorted_arr = sorted(arr, reverse=True)
# print("sorted_arr: ", sorted_arr)


def count_sort(arr):

    # assume array is positive
    largest = -1

    for num in arr:
        largest = max(largest, num)

    print("largest number is: ", largest)

    # create a frequency array; initially filled with ZERO
    count_arr = [0] * (largest+1)

    for j in range(len(arr)):
        # increment the index value by 1
        count_arr[arr[j]] += 1

    print("count array is: ", count_arr)

    j = 0
    for i in range(len(count_arr)):
        # until the value at an index is > 0
        while count_arr[i] > 0:
            arr[j] = i      # assign the value
            j += 1          # increment index
            count_arr[i] -= 1  # decrease frequency by 1

    return arr

arr = [5,8,3,1,1,6,8]

sorted_array = count_sort(arr)
print("sorted_array: ", sorted_array)