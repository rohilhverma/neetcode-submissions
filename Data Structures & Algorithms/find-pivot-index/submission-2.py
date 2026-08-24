class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        total = 0
        for num in nums:
            total += num
            prefix.append(total)
        for index in range(len(nums)):
            leftPrefix=rightPrefix=0
            if index == 0:
                leftPrefix = 0
            else:
                leftPrefix = prefix[index-1]
            if index > len(nums)-1:
                rightPrefix = 0
            else:
                rightPrefix = prefix[-1] - prefix[index]
            if (rightPrefix == leftPrefix):
                return index
        return -1
            