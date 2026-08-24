class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        iterator = 0
        countSet = set()
        hashset = set(nums)
        if (len(nums)) == 0:
            return 0
        for x in range(len(nums)):
            count = 1
            if nums[x] - 1 not in hashset:
                iterator = nums[x]
                while count <= len(nums):
                    if iterator + 1 not in hashset:
                        countSet.add(count)
                        break
                    else:
                        count += 1
                        iterator += 1
                countSet.add(0)        
        return max(countSet)
                    
                




        
        