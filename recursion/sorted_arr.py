def is_sorted(arr, i, n):
    if i == n-1:
        return True
    if arr[i] < arr[i+1] and is_sorted(arr, i+1, n):
        return True
    else:
        print(arr[i], arr[i+1])
        return False
    
arr = [1,2,3,7,4,5]
n = len(arr)
output = is_sorted(arr, 0, n)
print(output)