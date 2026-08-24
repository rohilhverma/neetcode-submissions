class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (k == len(nums)):
            return nums
        nums.reverse()
        k = k % len(nums)
        a,b=0,k-1
        while a<b:
            nums[a], nums[b]=nums[b],nums[a]
            a+=1
            b-=1
        a,b=(k)%len(nums),len(nums)-1
        while a<b:
            nums[a], nums[b] = nums[b], nums[a]
            a+=1
            b-=1
        return nums