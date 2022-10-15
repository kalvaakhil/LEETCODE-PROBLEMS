#https://practice.geeksforgeeks.org/problems/shortest-path-in-a-binary-maze-1655453161/1
from typing import List
import heapq
from heapq import *
class Solution:
    def shortestPath(self, grid: List[List[int]], source: List[int], destination: List[int]) -> int:
        source, destination = tuple(source), tuple(destination)
        q = [(0, source)]
        costs = {source}
        m, n = len(grid), len(grid[0])
        while q:
            cost0, (r0, c0) = heappop(q)
            if (r0, c0) == destination:
                return cost0
                
            ncost = cost0+1
            if r0+1 < m and grid[r0+1][c0] == 1 and (r0+1, c0) not in costs:
                    costs.add((r0+1, c0))
                    heappush(q, (ncost, (r0+1, c0)))
            if r0-1 >= 0 and grid[r0-1][c0] == 1 and (r0-1, c0) not in costs:
                    costs.add((r0-1, c0))
                    heappush(q, (ncost, (r0-1, c0)))
                    
            if c0+1 < n and grid[r0][c0+1] == 1 and (r0, c0+1) not in costs:
                    costs.add((r0, c0+1))
                    heappush(q, (ncost, (r0, c0+1)))
            if c0-1 >= 0 and grid[r0][c0-1] == 1 and (r0, c0-1) not in costs:
                    costs.add((r0, c0-1))
                    heappush(q, (ncost, (r0, c0-1)))
                    
        return -1
