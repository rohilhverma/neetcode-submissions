class StockSpanner:
    
    
    def __init__(self):
        self.lst=[]

    def next(self, price: int) -> int:
        if not self.lst:
            self.lst.append(price)
            return 1
        if self.lst:
            temp=[]
            var=1
            while self.lst and self.lst[-1] <= price:
                temp.append(self.lst.pop())
                var+=1
            for x in temp:
                self.lst.append(x)
            self.lst.append(price)
            return var
            






# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)