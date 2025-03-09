class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        haha = max(nums)
        ans = 0
        for i in range(k):
            ans += haha+i
        return ans