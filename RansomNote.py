# -*- coding: utf-8 -*-
"""
Ransom Note
LeetCode
5/3/2020

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.
Each letter in the magazine string can only be used once in your ransom note.
Note:
You may assume that both strings contain only lowercase letters. 
"""

def filldic (l):
    dic = {}
    for elt in l:
        if elt in dic:
            dic[elt] += 1
        else:
            dic[elt] = 1 
    return dic

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        md = filldic(magazine)
        rd = filldic(ransomNote)

        for letter, count in rd.items():
            if letter not in md:
                return False
            else:
                if count <= md[letter]:
                    pass
                else:
                    return False
        return True