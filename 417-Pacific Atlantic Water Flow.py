# -*- coding: utf-8 -*-
# @Author  : James Hu
# @Time    : 31/8/2022 1:12 PM
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        m, n = len(heights), len(heights[0])
        pacific = [[False] * n for _ in range(m)]
        atlantic = [[False] * n for _ in range(m)]

        def flow(grid, i, j, x, y):
            if i==x and j==y:

            if i == 0 or j == 0:
                pacific[x][y] = True
                if i == m - 1 or j == n - 1:
                    atlantic[x][y] = True
                return
            if i == m - 1 or j == n - 1:
                atlantic[x][y] = True
                if i == 0 or j == 0:
                    pacific[x][y] = True
                return
            if grid[i - 1][j] <= grid[i][j]:
                flow(grid, i - 1, j, x, y)
            if grid[i + 1][j] <= grid[i][j]:
                flow(grid, i + 1, j, x, y)
            if grid[i][j - 1] <= grid[i][j]:
                flow(grid, i, j - 1, x, y)
            if grid[i][j + 1] <= grid[i][j]:
                flow(grid, i, j + 1, x, y)
            return

        for i in range(m):
            for j in range(n):
                flow(heights, i, j,i,j)
        print(pacific)
        print(atlantic)
        res = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res


s = Solution()
heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(s.pacificAtlantic(heights))
