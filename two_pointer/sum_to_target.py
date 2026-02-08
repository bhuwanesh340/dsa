'''
Function to find elements whose sum is equal to target
'''

def arrayPairSum(arr, target):
    # Sort the array to use two-pointer technique
    arr.sort()
    left, right = 0, len(arr) - 1
    pairs = []

    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return pairs

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6,8]
    target = 7
    result = arrayPairSum(arr, target)
    print(f"Pairs that sum to {target}: {result}")