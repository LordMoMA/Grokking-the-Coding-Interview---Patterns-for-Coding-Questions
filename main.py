class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def maxPathSum(root):
        sum = float("-inf")
        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            leftSum = max(left, 0)
            rightSum = max(right, 0)
            localSum = leftSum + rightSum + root.val
            sum = max(sum, localSum)
            return max(leftSum, rightSum) + root.val
        dfs(root)
        return sum

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # root.left.left = TreeNode(6)
    # root.right.right = TreeNode(6)

    print("max sum: " + str(maxPathSum(root)))
    # print("max sum: " + str(find_path(root, [1, 1, 6])))

main()

