class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_path(root, sequence):
    
    return dfs(root, sequence, 0)

def dfs(root, sequence, i):
    if not root:
        return False
    length = len(sequence)
    if i >= length or sequence[i] != root.val:
        return False
    if not root.left and not root.right and i == length - 1:
        return True

    return dfs(root.left, sequence, i+1) or dfs(root.right, sequence, i+1)

def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.right.right = TreeNode(6)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))

main()

