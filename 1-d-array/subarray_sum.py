
def print_subarr_sum(arr, n):
    max_sum = 0
    for i in range(0, n):
        for j in range(i, n):
            subarr_sum = 0

            for k in range(i,j+1):
                subarr_sum += arr[k]

            # if subarr_sum > max_sum:
            #     max_sum = subarr_sum

            max_sum = max(subarr_sum, max_sum)

    return max_sum


# arr = [10,20,30,40,50,60]
arr = [-2,3,4,-1,5,-12,6,1,3]
n = len(arr)

max_sum = print_subarr_sum(arr,n)
print(max_sum)