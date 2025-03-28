# Last updated: 29/3/2025, 1:02:03 am
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = [0] * len(queries)
        sorted_queries = sorted((val, idx) for idx, val in enumerate(queries))
        min_heap = [(grid[0][0], 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        points = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for query_value, idx in sorted_queries:
            while min_heap and min_heap[0][0] < query_value:
                val, x, y = heappop(min_heap)
                points += 1
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                        heappush(min_heap, (grid[nx][ny], nx, ny))
                        visited[nx][ny] = True
            result[idx] = points
        return result