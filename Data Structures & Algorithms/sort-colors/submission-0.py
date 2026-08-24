class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = [0,0,0]
        for x in nums:
            colors[x] += 1
        i = 0
        for y in range(len(colors)):
            for z in range(colors[y]):
                nums[i] = y
                i += 1
        return nums

        