class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if (k % len(nums)==0):return nums
        nums.reverse()

        l,r=k%len(nums),len(nums)-1
        a,b=0,k%len(nums)-1

        while l < r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1
        while a<b:
            nums[a],nums[b]=nums[b],nums[a]
            a+=1
            b-=1
        return nums


        