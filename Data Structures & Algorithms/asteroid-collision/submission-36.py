class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lst=[]

        for x in asteroids:
            if lst and lst[-1]>0 and x < 0:
                while lst and lst[-1]>0 and lst[-1] < abs(x):
                    lst.pop()
                if not lst:
                    lst.append(x)
                    continue
                if lst[-1] > abs(x):
                    continue
                elif lst[-1] == abs(x):
                    lst.pop()
                    continue
                lst.append(x)
            else:
                lst.append(x)
        return lst