class MinStack:
    lst=None
    m=None
    def __init__(self):
        self.lst=[]
        self.m=[]

    def push(self, val: int) -> None:
        self.lst.append(val)

        if not self.m:
            self.m.append(val)
        else:
            self.m.append(min(self.m[-1], val))
        
    def pop(self) -> None:
        self.m.pop()
        return self.lst.pop()

    def top(self) -> int:
        return self.lst[-1]
        

    def getMin(self) -> int:
        return self.m[-1]