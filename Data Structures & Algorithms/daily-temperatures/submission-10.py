class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0]*len(temperatures)
        lst=[]
        for x in range(len(temperatures)):
            if lst and lst[-1][0] < temperatures[x]:
                temp=[]
                while lst and lst[-1][0] < temperatures[x]:
                    y = lst.pop()
                    result[y[1]] = x-y[1]

            lst.append((temperatures[x], x))
        return result
            