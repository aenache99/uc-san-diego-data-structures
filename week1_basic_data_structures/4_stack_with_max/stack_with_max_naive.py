import sys


class StackWithMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.max_stack or value >= self.max_stack[-1]:
            self.max_stack.append(value)

    def pop(self):
        if not self.stack:
            return
        if self.stack[-1] == self.max_stack[-1]:
            self.max_stack.pop()
        self.stack.pop()

    def max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline().strip())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.push(int(query[1]))
        elif query[0] == "pop":
            stack.pop()
        elif query[0] == "max":
            max_val = stack.max()
            print(max_val if max_val is not None else "None")
        else:
            raise NotImplementedError()
