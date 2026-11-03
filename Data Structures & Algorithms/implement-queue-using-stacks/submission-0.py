class MyQueue:

    def __init__(self):
        self.inward=[]
        self.outward=[]

    def push(self, x: int) -> None:
        self.inward.append(x)

    def pop(self) -> int:
        if not self.outward:
            while self.inward:
                self.outward.append(self.inward.pop())
        return self.outward.pop()

    def peek(self) -> int:
        if not self.outward:
            while self.inward:
                self.outward.append(self.inward.pop())
        return self.outward[-1]

    def empty(self) -> bool:
        return max(len(self.inward),len(self.outward))==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()