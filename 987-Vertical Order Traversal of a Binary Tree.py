# Definition for a binary tree node.
from collections import defaultdict
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d = defaultdict(list)

        def func(node, y, x):
            if not node:
                return
            if d[x] == []:
                d[x] = defaultdict(list)
            d[x][y].append(node.val)
            left, right = node.left, node.right
            func(left, y + 1, x - 1)
            func(right, y + 1, x + 1)

        func(root, 0, 0)
        res = []
        key = list(d.keys())
        print(d)
        key.sort()
        for i in key:
            key2 = list(d[i].keys())
            res.append([])
            key2.sort()
            for j in key2:
                d[i][j].sort()
                res[-1].extend(d[i][j])
        return res
