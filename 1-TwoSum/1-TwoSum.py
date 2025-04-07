# Last updated: 7/4/2025, 10:36:39 am
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            diff[target-nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in diff:
                if i != diff[nums[i]]:
                    return [i,diff[nums[i]]]