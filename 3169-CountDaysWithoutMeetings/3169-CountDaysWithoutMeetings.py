# Last updated: 24/3/2025, 10:43:53 am
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        ans = end = 0
        meetings.sort()
        for i, j in meetings:
            if i > end + 1:
                ans += i - end - 1
            end = max(end, j)
        ans += days - end
        return ans