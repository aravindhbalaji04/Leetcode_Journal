# Last updated: 8/4/2025, 2:24:29 pm
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        cnt = 0
        while len(nums)!= len(list(set(nums))):
            cnt += 1
            op = 3
            while len(nums) and op:
                nums.remove(nums[0])
                op -= 1
        return cnt