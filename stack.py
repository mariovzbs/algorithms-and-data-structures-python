class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def main():
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Peek:", stack.peek())
    print("Pop:", stack.pop())
    print("Size:", stack.size())
    print("Is empty:", stack.is_empty())


main()
