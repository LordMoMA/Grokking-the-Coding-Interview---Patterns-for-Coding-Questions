class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_path(root, sequence):
    num = ''.join(map(str, sequence))

    return num == str(dfs(root, 0))

def dfs(root, res):
    if not root:
        return 0
    res = res * 10 + root.val
    if not root.left and not root.right:
        return res
    return dfs(root.left, res) or dfs(root.right, res)

def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.right.right = TreeNode(6)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))

main()

