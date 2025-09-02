def last_occur(arr, key, n):
    if n == 0:
        return -1
    sub_index = last_occur(arr[1:], key, n - 1)
    if sub_index == -1:
        # Check the first element if not found in the rest of subarray
        if arr[0] == key:
            return 0
        else:
            return -1
    else:
        # If found in the subarray, adjust index +1
        print(f"sub_index: {sub_index}")
        return sub_index + 1

array = [1, 2, 3, 4, 2, 5]
key = 5
n = len(array)
result = last_occur(array, key, n)
print(f"Last occurrence of {key} is at index: {result}")