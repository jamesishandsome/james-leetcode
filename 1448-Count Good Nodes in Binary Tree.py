# -*- coding: utf-8 -*-
# @Author  : James Hu
# @Time    : 1/9/2022 2:31 PM
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if (root.left is None and root.right is None):
            return 1

        def goodin3(root, maxval, result):
            print(maxval)
            print(root.val)
            left = root.left
            right = root.right
            if root.val > maxval:
                maxval = root.val
            if left is not None:
                if (left.val >= maxval):
                    result += 1
                result = goodin3(left, maxval, result)

            if right is not None:
                if (right.val >= maxval):
                    result += 1
                result = goodin3(right, maxval, result)
            return result

        return goodin3(root, root.val, 1)