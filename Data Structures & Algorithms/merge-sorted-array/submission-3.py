class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x = m+n-1
        y = m-1
        z = n-1
        while x >= 0:
            if y>=0 and z >=0 and nums1[y] >= nums2[z]:
                nums1[x] = nums1[y]
                y-=1
            elif z>=0:
                nums1[x] = nums2[z]
                z-=1
            x -= 1