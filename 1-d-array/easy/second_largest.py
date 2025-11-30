class Solution:
    def secondLargestElement(self, nums):
        if type(nums) != list:
            nums = nums.split(",")

        if len(nums) <= 1:
            return -1
        
        largest = float('-inf')
        second_largest = float('-inf')
        for i in range(len(nums)):
            # print("current: ", nums[i])
            if nums[i] > largest:
                second_largest = largest
                largest = nums[i]
            elif nums[i] > second_largest and nums[i] != largest:
                second_largest = nums[i]

                # print("largest: {}, second_largest: {}".format(largest, second_largest))
            
        return -1 if second_largest == float('-inf') else second_largest


case1 = [8, 8, 7, 6, 5]
case2 = [3, 3, 0, 99, -40]
case3 = [10,10,10,10]
sol = Solution()
res1 = sol.secondLargestElement(case1)
print("The second largest number in the array is:", res1)
res2 = sol.secondLargestElement(case2)
print("The second largest number in the array is:", res2)
res3 = sol.secondLargestElement(case3)
print("The second largest number in the array is:", res3)