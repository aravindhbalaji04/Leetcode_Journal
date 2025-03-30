# Last updated: 30/3/2025, 8:48:27 am
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n, m = len(skill), len(mana)
        grid = [0]*n
        grid[0] = skill[0]*mana[0]
        for i in range(1,n):
            grid[i] = grid[i-1]+skill[i]*mana[0]
        for i in range(1,m):
            temp = grid[-1]
            for j in range(n-1, -1, -1):
                val = temp-skill[j]*mana[i]
                if val >= grid[j]:
                    temp = val
                else:
                    temp = grid[j]
            grid[0] = temp+skill[0]*mana[i]
            for j in range(1, n):
                grid[j] = grid[j-1]+skill[j]*mana[i]
        return grid[-1]