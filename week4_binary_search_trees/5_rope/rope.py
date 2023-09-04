import sys


class Rope:
    def __init__(self, s):
        self.s = s

    def result(self):
        return self.s

    def process(self, i, j, k):
        # Extract the substring to be moved
        sub = self.s[i:j + 1]

        # Remove the extracted substring from the original string
        self.s = self.s[:i] + self.s[j + 1:]

        # Insert the extracted substring at position k
        self.s = self.s[:k] + sub + self.s[k:]


rope = Rope(sys.stdin.readline().strip())
q = int(sys.stdin.readline())
for _ in range(q):
    i, j, k = map(int, sys.stdin.readline().strip().split())
    rope.process(i, j, k)
print(rope.result())
