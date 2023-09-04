import sys
import threading

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeOrders:
    def read(self):
        self.n = int(input())
        self.key = [0 for _ in range(self.n)]
        self.left = [0 for _ in range(self.n)]
        self.right = [0 for _ in range(self.n)]
        for i in range(self.n):
            a, b, c = map(int, input().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []
        self._inOrder(0)  # Start from the root
        return self.result

    def _inOrder(self, root):
        if root == -1:
            return
        self._inOrder(self.left[root])
        self.result.append(self.key[root])
        self._inOrder(self.right[root])

    def preOrder(self):
        self.result = []
        self._preOrder(0)  # Start from the root
        return self.result

    def _preOrder(self, root):
        if root == -1:
            return
        self.result.append(self.key[root])
        self._preOrder(self.left[root])
        self._preOrder(self.right[root])

    def postOrder(self):
        self.result = []
        self._postOrder(0)  # Start from the root
        return self.result

    def _postOrder(self, root):
        if root == -1:
            return
        self._postOrder(self.left[root])
        self._postOrder(self.right[root])
        self.result.append(self.key[root])


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
