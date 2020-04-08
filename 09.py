class CQueue:

    def __init__(self):
        self.stack_push = []
        self.stack_pop = []

    def appendTail(self, value: int) -> None:
        while self.stack_pop:
            self.stack_push.append(self.stack_pop.pop())
        self.stack_push.append(value)


    def deleteHead(self) -> int:
        while self.stack_push:
            self.stack_pop.append(self.stack_push.pop())
        if self.stack_pop is None:
            return -1
        return self.stack_pop.pop()
    



# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()