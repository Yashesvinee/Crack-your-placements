import collections as ct
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        c = ct.Counter(nums)
        val = list(c.values())
        i = val.index(max(val))
        return list(c.keys())[i]
