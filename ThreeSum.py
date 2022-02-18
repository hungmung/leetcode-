class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3: return []
        from itertools import combinations
        rtn = []
        for c in filter(lambda x: sum(x)==0, combinations(nums, 3)):
            v = sorted(list(c))
            if v not in rtn:
                rtn.append(v)
        return rtn
