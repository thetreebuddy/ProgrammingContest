# -*- coding: utf-8 -*-
"""
Number Complement
LeetCode
5/4/2020

Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.
Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/
"""

class Solution:
    def findComplement(self, num: int) -> int:
        comp = []
        for elt in bin(num)[2:]:
            if elt == '0':
                comp.append('1')
            if elt == '1':
                comp.append('0')

        comp = ''.join(comp)
        newi = int('0b'+comp, 2)
        
        return newi
