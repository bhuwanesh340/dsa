def all_occur(arr, key, n):
    if n == 0:
        return []
    sub_indices = all_occur(arr[1:], key, n - 1)
    print(f"sub_indices: {sub_indices}")
    if arr[0] == key:
        # If the first element matches the key, include index 0
        return [0] + [index + 1 for index in sub_indices]
    else:
        # If not, just adjust the indices from the subarray
        return [index + 1 for index in sub_indices]
    

array = [1, 2, 3, 2, 4, 2, 5]
key = 2
n = len(array)
result = all_occur(array, key, n)
print(f"All occurrences of {key} are at indices: {result}")