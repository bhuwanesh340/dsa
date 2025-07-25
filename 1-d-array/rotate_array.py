# K-Rotate
# Given an integer vector and a value k, your task is to rotate the array k times clockwise.

# Input Format
# In the function an integer vector and number k is passed.

# Output Format
# Return an integer vector.

# Sample Input
# {1, 3, 5, 7, 9}, x = 2

# Sample Output
# {7, 9, 1, 3, 5}

# Explanation
# After 1st rotation - {9, 1, 3, 5, 7}
# After 2nd rotation - {7, 9, 1, 3, 5}

def rotate_arr(arr,val):
    out = []

    for i in range(len(arr)-val, len(arr)):
        # print(arr[i])
        out.append(arr[i])

    for i in range(0, len(arr)-val):
        # print(arr[i])
        out.append(arr[i])

    return out

def rotate_arr_reverse_method(arr, k):
    # reverse first 0 to n-k part
    arr[0:len(arr)-k] = reversed(arr[0:len(arr)-k])

    # reverse  n-k to n part
    arr[len(arr)-k: len(arr)] = reversed(arr[len(arr)-k: len(arr)])

    # reverse full
    arr[:len(arr)] = reversed(arr[:len(arr)])

    return arr

arr = [1,2,3,4]
k = 2
rotated_arr = rotate_arr(arr, k)
print(rotated_arr)

# method 2: optimized

arr2 = [1,2,3,4,5,6,7,8]
k = 3
rotated_arr2 = rotate_arr_reverse_method(arr2, k)
print(rotated_arr2)

