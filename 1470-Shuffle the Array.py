# -*- coding: utf-8 -*-
# @Author  : James Hu
# @Time    : 29/8/2022 12:02 PM
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums[::2], nums[1::2] = nums[:n], nums[n:]
        return nums