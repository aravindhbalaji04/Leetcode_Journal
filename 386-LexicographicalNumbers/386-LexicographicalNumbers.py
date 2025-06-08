# Last updated: 8/6/2025, 4:52:50 am
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def helper(num, curr, n, arr):
            if curr > 9:
                return 
            t = num * 10 + curr
            if t <= n:
                ans.append(t)
                helper(t, 0, n, ans)
                helper(num, curr+1, n, ans)
        ans = []
        helper(0, 1, n, ans)
        return ans