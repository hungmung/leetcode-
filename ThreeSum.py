class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k,
        and nums[i] + nums[j] + nums[k] == 0.
        
        Notice that the solution set must not contain duplicate triplets.
        """
        if len(nums)<3: return []
        from itertools import combinations
        rtn = []
        for c in filter(lambda x: sum(x)==0, combinations(nums, 3)):
            v = sorted(list(c))
            if v not in rtn:
                rtn.append(v)
        return rtn
    # Note this solution is too slow and fails on test 315/318 on leetcode
