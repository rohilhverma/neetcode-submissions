class MyCircularQueue:

    def __init__(self, k: int):
        self.arr = [-1,]*k
        self.curr=0
        self.que=0

    def enQueue(self, value: int) -> bool:
        if min(self.arr) >= 0:
            return False
        self.arr[self.curr%len(self.arr)]=value
        self.curr+=1
        return True

    def deQueue(self) -> bool:
        if (self.arr[self.que%len(self.arr)] < 0): return False
        self.arr[self.que%len(self.arr)] = -1
        self.que+=1
        return True

    def Front(self) -> int:
        if (max(self.arr)==-1):return -1
        return self.arr[self.que%len(self.arr)]

    def Rear(self) -> int:
        if (max(self.arr)==-1):return -1
        return self.arr[(self.curr % len(self.arr)) -1]

    def isEmpty(self) -> bool:
        if max(self.arr)==-1:return True
        return False

    def isFull(self) -> bool:
        if min(self.arr)>=0:return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()