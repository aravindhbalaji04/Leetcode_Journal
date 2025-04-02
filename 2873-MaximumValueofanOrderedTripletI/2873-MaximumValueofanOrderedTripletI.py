# Last updated: 2/4/2025, 10:17:50 am
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        a = []
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    if i != j and j != k and i != k and k > j and j > i and k > i:
                        a.append((nums[i]-nums[j])*nums[k])
        if max(a) > 0:
            return max(a)
        else:
            return 0