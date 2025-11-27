class maxNumArrSolution:
    def largestElement(self, nums):
        if type(nums) == list:
            if len(nums) > 1:
                largest = nums[0]
                for i in range(1,len(nums)):
                    if nums[i] > largest:
                        largest = nums[i]
            else:
                largest = nums[0]
        else:
            temp_list = nums.split(",")
            if len(temp_list) > 1:
                largest = nums[0]
                for j in range(1,len(temp_list)):
                    if temp_list[j] > largest:
                        largest = temp_list[j]
            else:
                largest = nums[0]


        print("The largest number in the array is:", largest)
        return largest
    

max_num = maxNumArrSolution()

case1 = [3, 3, 6, 1]
max1 = max_num.largestElement(case1)

case2 = [3, 3, 0, 99, -40]
max2 = max_num.largestElement(case2)

case3 = [-1,-2,-3,-4]
max3 = max_num.largestElement(case3)