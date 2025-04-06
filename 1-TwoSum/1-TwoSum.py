# Last updated: 6/4/2025, 2:21:35 pm
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick = {}
        for i in range(len(nums)):
            if target-nums[i] in dick:
                return [dick[target-nums[i]], i]
            else:
                dick[nums[i]] = i