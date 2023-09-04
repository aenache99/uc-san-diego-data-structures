class TreeNode:
    def __init__(self):
        self.children = []


def compute_tree_height(parents):
    n = len(parents)
    nodes = [TreeNode() for _ in range(n)]
    root = None

    # Build the tree structure
    for child_index, parent_index in enumerate(parents):
        if parent_index == -1:
            root = nodes[child_index]
        else:
            nodes[parent_index].children.append(nodes[child_index])

    stack = [(root, 1)]  # Using a stack for iterative traversal, along with the depth

    max_height = 0

    while stack:
        node, depth = stack.pop()
        max_height = max(max_height, depth)

        for child in node.children:
            stack.append((child, depth + 1))

    return max_height


if __name__ == '__main__':
    n = int(input())
    parents = list(map(int, input().split()))
    tree_height = compute_tree_height(parents)
    print(tree_height)
