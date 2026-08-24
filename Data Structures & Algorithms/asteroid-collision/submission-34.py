class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        lst=[]
        destroyed = None
        for x in asteroids:
            destroyed = False
            if lst:
                if lst[-1] > 0 and x < 0:
                    while lst :
                        if lst[-1] < 0:
                            destroyed = False
                            break
                        if lst[-1] > abs(x):
                            destroyed = True
                            break
                        elif lst[-1] < abs(x):
                            lst.pop()
                            continue
                        else:
                            lst.pop()
                            destroyed = True
                            break
                    if not destroyed:
                        lst.append(x)
                else:
                    lst.append(x)
            else:
                lst.append(x)
        return lst