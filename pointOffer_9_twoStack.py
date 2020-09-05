class CQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def appendTail(self, value: int) -> None:
        self.s1.append(value)

    def deleteHead(self) -> int:
        if len(self.s1) == 0: return -1
        while self.s1:
            self.s2.append(self.s1.pop())
        tmp = self.s2.pop()
        while self.s2:
            self.s1.append(self.s2.pop())
        return tmp


if __name__ == "__main__":
    test = CQueue()
    test.appendTail(1)
    test.appendTail(3)
    test.appendTail(2)
    print(test.deleteHead())
    print(test.deleteHead())
