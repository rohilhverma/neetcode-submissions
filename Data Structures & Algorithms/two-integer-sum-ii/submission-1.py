class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        y = len(numbers)-1
        x = 0
        while x < y:
            if numbers[x] + numbers[y] == target:
                return [x+1,y+1]
            elif numbers[x] + numbers[y] > target:
                y -= 1
            elif numbers[x] + numbers[y] < target:
                x += 1
        