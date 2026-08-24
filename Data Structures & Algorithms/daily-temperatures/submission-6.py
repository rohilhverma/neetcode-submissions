class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        lst=[]
        result=[0,] * len(temperatures)
        for x in range(len(temperatures)):
            while lst and temperatures[lst[-1]] < temperatures[x]:
                result[lst[-1]] = x - lst[-1]
                lst.pop()
            lst.append(x)
        return result


