def first_occur(arr, n, key):
    if n == 0:
        return -1
    if arr[0] == key:
        return 0
    sub_index = first_occur(arr[1:], n - 1, key)
    if sub_index == -1:
        return -1
    else:
        return sub_index + 1
    

array = [1, 2, 3, 4, 2, 5]
key = 2
n = len(array)
result = first_occur(array, n, key)
print(f"First occurrence of {key} is at index: {result}")