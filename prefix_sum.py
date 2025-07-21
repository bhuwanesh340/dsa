def prefix_sum(arr, n):
    prefix_sum_arr = []
    prefix_sum_arr.append(arr[0])

    for i in range(1,n):
        # print(prefix_sum_arr)
        # print(prefix_sum_arr[i-1])
        # print(arr[i])
        prefix_sum_arr.append(prefix_sum_arr[i-1] + arr[i])

    print("prefix summ array: ", prefix_sum_arr)

    largest_sum = 0
    for i in range(0,n):
        for j in range(i,n):
            if i > 0:
                subarr_sum = prefix_sum_arr[j] - prefix_sum_arr[i-1]
            else:
                subarr_sum = prefix_sum_arr[j]
            
            print("i,j: {},{} ".format(i,j))
            print(subarr_sum)

            largest_sum = max(largest_sum, subarr_sum)
            print("******")

    return largest_sum


# arr = [10,20,30,40,50]
arr = [-2,3,4,-1,5,-12,6,1,3]

out = prefix_sum(arr, len(arr))
print(out)

