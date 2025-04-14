# Last updated: 14/4/2025, 11:54:08 am
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dick = {}
        for i in range(len(nums)):
            if target-nums[i] in dick:
                return [dick[target-nums[i]], i]
            else:
                dick[nums[i]] = i