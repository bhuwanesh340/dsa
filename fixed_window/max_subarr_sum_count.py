'''
find the count of subarrays of size le(arr) from array whose sum is greater than or equal to k
'''

def max_subarr_sum_count(arr, k):

    if len(arr) < k:
        return None
    
    max_len = 0
    sum = 0

    for i in range(len(arr)):
        for j in range(i, len(arr)):
            sum = sum + arr[j]
            if sum <= s:
                max_len = max(max_len, j-i+1)
            else:   
                break

    return max_len

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    k = 10
    max_len = max_subarr_sum_count(arr, k)
    print("Max length of subarray whose sum is less than or equal to k is: ", max_len)