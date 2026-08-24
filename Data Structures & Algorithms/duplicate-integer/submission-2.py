class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set()
        for x in nums:
            if x in duplicates:
                return True
            duplicates.add(x)
        return False
        