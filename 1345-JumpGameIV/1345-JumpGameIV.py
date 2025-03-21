// Last updated: 21/3/2025, 10:34:53 pm
class Solution:
    def minJumps(self, nums: List[int]) -> int:
        adjList = defaultdict(list)
        for ind, adj in enumerate(nums):
            if adj in adjList:
                adjList[adj].append(ind)
            else:
                adjList[adj] = [ind]
        queue = deque([(0,0)])
        visited = set([0])
        while queue:
            node, op = queue.popleft()
            if node == len(nums)-1:
                return op
            if node + 1 < len(nums) and node + 1 not in visited:
                visited.add(node + 1)
                queue.append((node+1, op+1))
            if node - 1 > -1 and node - 1 not in visited:
                visited.add(node - 1)
                queue.append((node-1, op+1))
            for i in adjList[nums[node]]:
                if i != node and i not in visited:
                    queue.append((i, op+1))
                    visited.add(i)
            adjList[nums[node]] = []