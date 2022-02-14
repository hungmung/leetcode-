# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays. 
# 
# The overall run time complexity should be O(log (m+n)).
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        merged = sorted(nums1)
        if len(merged)%2==0:
            pos = len(merged)/2
            median = (float(merged[pos]+merged[pos-1]))/2
        else:
            pos = int(len(merged)/2 + 0.5)
            median = merged[pos]
        return median
