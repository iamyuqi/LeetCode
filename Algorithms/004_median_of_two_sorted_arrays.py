#There are two sorted arrays nums1 and nums2 of size m and n respectively.

#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

#You may assume nums1 and nums2 cannot be both empty.

#Example 1:

#nums1 = [1, 3]
#nums2 = [2]

#The median is 2.0
#Example 2:

#nums1 = [1, 2]
#nums2 = [3, 4]

#The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = sorted(nums1 + nums2)
        l = len(s)
        if l == 1:
            m = s[0]
        elif l % 2 == 1:
            m = s[int(l/2-0.5)]
        else:
            m = (s[int(l/2)-1]+s[int(l/2)])/2
        return float(m)