class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lst = []
        for x in asteroids:
            if (lst and x < 0 and lst[-1] > 0):
                while lst and x < 0 and lst[-1] > 0:
                    if lst[-1] < (x * -1):
                        lst.pop()
                    else:
                        break
                if len(lst) == 0 or lst[-1] < 0:
                    lst.append(x)
                elif lst[-1] > 0 and lst[-1] > (x * -1):
                    continue
                else:
                    lst.pop()
            else:
                lst.append(x)    
        return lst