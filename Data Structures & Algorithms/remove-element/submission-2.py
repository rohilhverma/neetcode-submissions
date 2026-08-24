class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        y = len(nums)-1
        while x <= y:
            if nums[x] == val:
                nums[x] = nums[y]
                y -= 1
            else:
                x += 1
        return x