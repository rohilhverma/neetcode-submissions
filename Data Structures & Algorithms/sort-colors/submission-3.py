class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lst = [0,0,0]
        for x in range(len(nums)):
            lst[nums[x]] += 1
        y = 0
        for x in range(len(nums)):
            while lst[y] == 0:
                y += 1
            nums[x] = y
            lst[y] -= 1



