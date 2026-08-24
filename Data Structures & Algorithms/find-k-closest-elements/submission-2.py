class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        a,b=0,len(arr)-1

        while b-a+1 > k:
            if abs(arr[b]-x) < abs(arr[a]-x):
                a+=1
            else:
                b-=1
        return arr[a:b+1]