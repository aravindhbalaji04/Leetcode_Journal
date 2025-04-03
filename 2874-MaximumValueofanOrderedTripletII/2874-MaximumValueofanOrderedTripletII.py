# Last updated: 3/4/2025, 1:58:39 pm
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefix = []
        mx = -inf
        for n in nums:
            mx = max(mx, n)
            prefix.append(max(mx-n, 0))
        
        suffix = []
        for n in reversed(nums):
            suffix.append(n if not suffix else max(n, suffix[-1]))
        suffix[:] = reversed(suffix)

        return max(prefix[i]*suffix[i+1] for i in range(1,len(nums)-1))