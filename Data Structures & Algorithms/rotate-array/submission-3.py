class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k == 0:
            return nums
        k = k % len(nums)
        x, y = 0, len(nums)-1
        while x < y:
            nums[x], nums[y] = nums[y], nums[x]
            x+=1
            y-=1
        x, y = 0, k - 1
        while x < y:
            nums[x], nums[y] = nums[y], nums[x]
            x += 1
            y -=1
        x, y = k, len(nums)-1
        while x<y:
            nums[x], nums[y] = nums[y], nums[x]
            x +=1
            y-=1
        return nums

    
