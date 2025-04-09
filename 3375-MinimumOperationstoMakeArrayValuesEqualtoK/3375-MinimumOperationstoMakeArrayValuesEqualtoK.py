# Last updated: 9/4/2025, 9:07:38 am
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int: 
        if k > min(nums):
            return -1
        else:
            cnt = len(list(set(nums)))
            if k in nums: 
                cnt -= 1
            return cnt