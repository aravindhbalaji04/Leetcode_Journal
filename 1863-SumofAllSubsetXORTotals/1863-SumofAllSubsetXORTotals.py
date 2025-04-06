# Last updated: 6/4/2025, 1:38:50 pm
class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        for i in range(len(nums) + 1):
            subsets = itertools.combinations(nums, i)
            for subset in subsets:
                xor = 0
                for num in subset:
                    xor ^= num
                total += xor
        return total