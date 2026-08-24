class StockSpanner:

    def __init__(self):
        self.stack=[]
        

    def next(self, price: int) -> int:
        spanner=1
        while self.stack and self.stack[-1][0] <= price:
            spanner += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, spanner])
        return spanner


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)