# Last updated: 24/3/2025, 11:01:38 am
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for i in stones:
            heapq.heappush(max_heap, -i)
        while len(max_heap) != 1:
            print(max_heap)
            a, b = heapq.heappop(max_heap), heapq.heappop(max_heap)
            heapq.heappush(max_heap, abs(max(a,b))+min(a,b))
        return abs(max_heap[0])