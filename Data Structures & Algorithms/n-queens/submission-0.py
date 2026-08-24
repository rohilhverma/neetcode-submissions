class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        self.returnArr=[]
        self.tracker=[-1]*n

        def help(i, lst):
            if i == n:
                self.returnArr.append(lst.copy())
                return
            
            for x in range(n):
                valid=True
                for y in range(i):
                    if self.tracker[y] == x or abs(self.tracker[y] - x) == abs(y-i):
                        valid=False
                if valid:
                    s = "." * x + "Q" + "." * (n-x-1)
                    self.tracker[i] = x
                    lst.append(s)
                    help(i+1, lst)
                    lst.pop()
                    
            
        help(0, [])
        return self.returnArr
                    

                             

