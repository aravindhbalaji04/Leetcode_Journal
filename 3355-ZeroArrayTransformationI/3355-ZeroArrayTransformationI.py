# Last updated: 20/5/2025, 6:56:53 pm
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0]*(len(nums)+1)
        for query in queries:
            diff[query[0]] -= 1
            diff[query[-1]+1] += 1
        total = 0
        for i in range(len(nums)):
            total += diff[i]
            if nums[i] + total > 0:
                return False
        return True