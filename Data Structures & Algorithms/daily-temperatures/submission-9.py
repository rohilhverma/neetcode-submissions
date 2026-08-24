class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result=[0,]*len(temperatures)
        t=[]

        """
        Define result array,len of temperatures, stores number of days after the i'th day, till a 
        warmer temperature appears. 

        t represents a monotonic stack that'll be used to track decrementing temperatures. If a temp is 
        decreasing, add it, otherwise pop the stack, take the difference in days, save it to result, 
        and add to stack.


        """


        for x in range(len(temperatures)):
            if t and t[-1][0]<temperatures[x]:
                while t and t[-1][0]<temperatures[x]:
                    z = t.pop()
                    result[z[1]]= x-z[1]
            t.append((temperatures[x], x))

        return result
