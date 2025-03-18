class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = [amount+1]*(amount+1)
        ans[0] = 0
        for i in range(1, amount+1):
            for j in coins:
                if i - j >= 0:
                    ans[i] = min(ans[i], 1+ans[i-j])
        if ans[-1] != amount + 1:
            return ans[-1]
        return -1