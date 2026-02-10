'''
find the max sum of subarray of size k from array
'''

def max_sum_subarray_size_k(arr, k):

    if len(arr) < k:
        return None
    
    subarr_sum = []
    
    max_sum = 0
    current_sum = sum(arr[:k])

    subarr_sum.append(current_sum)
    max_sum = current_sum
    left = 0
    right = k-1
    while right<len(arr)-1:
        current_sum = current_sum - arr[left]
        left = left + 1
        right = right + 1
        current_sum = current_sum + arr[right]

        subarr_sum.append(current_sum)
        max_sum = max(max_sum, current_sum)

    print(f"Sum of subarrays of size {k} are: {subarr_sum}")
    print("Max sum of subarray of size k is: ", max_sum)
    return max_sum

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    k = 3
    max_sum_subarray_size_k(arr, k)


