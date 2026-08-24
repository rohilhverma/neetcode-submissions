class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1

        while l<=r:
            mid=(l+r)//2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                lst=matrix[mid]
                l,r=0,len(lst)-1
                while l<=r:
                    mid=(l+r)//2
                    if lst[mid]>target:
                        r=mid-1
                    elif lst[mid]<target:
                        l=mid+1
                    else:
                        return True
    
            elif matrix[mid][-1] < target or matrix[mid][0] < target:
                l=mid+1
            else:
                r=mid-1
        
        return False

