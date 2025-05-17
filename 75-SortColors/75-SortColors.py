# Last updated: 17/5/2025, 8:28:35 pm
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        a, b = 0, len(nums)-1
        arr = nums.copy()
        for i in range(len(nums)):
            nums[i] = 1
        for i in range(len(arr)):
            if arr[i] == 0:
                nums[a] = 0
                a += 1
            elif arr[i] == 2:
                nums[b] = 2
                b -= 1
        return nums