class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        

        for x in range(len(nums)):
            y=x+1
            while y < len(nums):
                if nums[x] == nums[y] and abs(y-x) <= k:
                    return True
                y+=1
        return False