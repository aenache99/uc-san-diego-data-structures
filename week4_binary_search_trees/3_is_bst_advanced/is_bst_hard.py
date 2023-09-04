import sys
import threading

sys.setrecursionlimit(10 ** 8)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class Node:
    def __init__(self, key=0, left=-1, right=-1):
        self.key = key
        self.left = left
        self.right = right


def is_bst_util(tree, node_index, _min, _max):
    if node_index == -1:
        return True

    if tree[node_index].key < _min or tree[node_index].key >= _max:
        return False

    return (
            is_bst_util(tree, tree[node_index].left, _min, tree[node_index].key) and
            is_bst_util(tree, tree[node_index].right, tree[node_index].key, _max)
    )


def is_binary_search_tree(tree):
    if not tree:
        return True

    return is_bst_util(tree, 0, float('-inf'), float('inf'))


def main():
    nodes = int(input())

    tree = []

    for _ in range(nodes):
        key, left, right = map(int, input().split())
        tree.append(Node(key, left, right))

    if is_binary_search_tree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


if __name__ == "__main__":
    threading.Thread(target=main).start()
