class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                nums[i] = 1
                op += 1
                if nums[i+1]:
                    nums[i+1] = 0
                else:
                    nums[i+1] = 1
                if nums[i+2]:
                    nums[i+2] = 0
                else:
                    nums[i+2] = 1
        if all(nums):
            return op
        return -1