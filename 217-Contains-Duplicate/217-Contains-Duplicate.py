from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_n = set()
        for i in range(len(nums)):
            if nums[i] in set_n:
                return True
            set_n.add(i)
        return False