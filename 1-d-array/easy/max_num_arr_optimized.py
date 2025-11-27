class maxNumArrSolution:
    def largestElement(self, nums):
        if type(nums) != list:
            nums = nums.split(",")

        if len(nums) == 1:
            return nums[0]
        else:
            largest = nums[0]
            for i in range(1,len(nums)):
                if nums[i] > largest:
                    largest = nums[i]
                    
        print("The largest number in the array is:", largest)
        return largest
    

max_num = maxNumArrSolution()

case1 = [3, 3, 6, 1]
max1 = max_num.largestElement(case1)

case2 = [3, 3, 0, 99, -40]
max2 = max_num.largestElement(case2)

case3 = [-1,-2,-3,-4]
max3 = max_num.largestElement(case3)