#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

#Example 1:
#Input: "babad"
#Output: "bab"
#Note: "aba" is also a valid answer.

#Example 2:
#Input: "cbbd"
#Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        idxs = []
        for char in s:
            idx = []
            for i, x in enumerate(s):
                if char == x:
                    idx.append(i)
                    if len(idx) == 1:
                        continue

                    # l1 = [j-i for i, j in zip(ind[:-1], ind[1:])]
                    # i1, i2 = ind[l1.index(max(l1))], ind[l1.index(max(l1))+1]
        return s[ind1:ind2+1]
