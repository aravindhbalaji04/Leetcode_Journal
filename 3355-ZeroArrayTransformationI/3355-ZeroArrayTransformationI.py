# Last updated: 20/5/2025, 6:38:24 pm
class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        diff = [0] * (n + 1)
        for l, r in queries:
            diff[l] -= 1
            if r + 1 < n:
                diff[r + 1] += 1
        curr = 0
        for i in range(n):
            curr += diff[i]
            if nums[i] + curr > 0:
                return False
        return True