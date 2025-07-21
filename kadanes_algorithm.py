def kadanes_subarr_sum(arr,n):
    current_sum = 0
    max_sum = 0

    for i in range(0,n):
        current_sum += arr[i]
        if current_sum < 0:
            current_sum = 0

        max_sum = max(max_sum, current_sum)

    return max_sum


arr = [-2,3,4,-1,5,-12,6,1,3]

out = kadanes_subarr_sum(arr,len(arr))
print(out)