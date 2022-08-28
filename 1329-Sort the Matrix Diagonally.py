from collections import defaultdict


class Solution:
    def diagonalSort(self, mat):
        m, n = len(mat), len(mat[0])
        new = defaultdict(list)
        for i in range(m):
            for j in range(n):
                new[i - j].append(mat[i][j])
        for k in new:
            new[k].sort(reverse=True)
        for i in range(m):
            for j in range(n):
                mat[i][j] = new[i - j].pop()
        return mat
