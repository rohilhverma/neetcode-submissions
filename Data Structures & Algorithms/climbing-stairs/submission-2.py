class Solution:
    def climbStairs(self, n: int) -> int:
        dct={}
        dct = {2:2,1:1}
        def help(n, dct):
            if n in dct:
                return dct[n]
            else:
                dct[n] = help(n-1, dct) + help(n-2, dct)
            return dct[n]
        return help(n, dct)
