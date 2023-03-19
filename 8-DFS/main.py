"""
112. Path Sum

Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

A leaf is a node with no children.

https://leetcode.com/problems/path-sum/description/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, sum):
        if root is None:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True

        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)

## solution2 

def hasPathSum(self, root, sum):
        if not root:
            return False

        if not root.left and not root.right and root.val == sum:
            return True
        
        sum -= root.val

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)  

# Time Complexity: O(n)
# Space Complexity: O(n)

################################################################
################################################################
################################################################

"""
113. Path Sum II


Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. 
Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Input: root = [1,2,3], targetSum = 5
Output: []

https://leetcode.com/problems/path-sum-ii/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: List[List[int]]
        """
        result = []
        self.dfs(root, [], sum, result)
        return result

    def dfs(self, root, path, sum, result):
        if not root:
            return
        path.append(root.val)
        if root.val == sum and not root.left and not root.right:
            #result.append(path[:])
            result.append(list(path))
        else: 
            self.dfs(root.left, path, sum - root.val, result) 
            self.dfs(root.right, path, sum - root.val, result)
        path.pop()

# Time Complexity: O(n^2)
# Space Complexity: O(n)     

################################################################
################################################################
################################################################


"""
257. Binary Tree Paths

Problem 1: Given a binary tree, return all root-to-leaf paths.

Solution: We can follow a similar approach. We just need to remove the “check for the path sum”.

Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        self.dfs(root, "", result)
        return result
        
    
    def dfs(self, root, path, result):
        if not root:
            return None
        if not root.left and not root.right:
            result.append(path + str(root.val))
        if root.left:
            self.dfs(root.left, path + str(root.val) + "->", result)
        if root.right:
            self.dfs(root.right, path + str(root.val) + "->", result)

# solution2:

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        return self.dfs(root, "")
    
    def dfs(self, root, path):
        if not root:
            return []
        path += str(root.val)
        if not root.left and not root.right:
            return [path]
        path += "->"
        return self.dfs(root.left, path) + self.dfs(root.right, path)
################################################################
################################################################
################################################################

'''
124. Binary Tree Maximum Path Sum

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

Solution Explanation:
https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/603423/python-recursion-stack-thinking-process-diagram/
https://www.youtube.com/watch?v=Hr5cWUld4vU&t=761s
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float("-inf")
        
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            left = max(left, 0)
            right = max(right, 0)
            res = max(left + right + node.val, res)
            return max(left, right) + node.val
        
        dfs(root)
        return res
# time O(n) space O(height of the tree) or O(h) or O(logn) if it's a balanced binary 

'''
129. Sum Root to Leaf Numbers
https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.

Input: root = [1,2,3]
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)

    def dfs(self, node, path_sum):
        if not node:
            return 0
        path_sum = 10 * path_sum + node.val

        if not node.left and not node.right:
            return path_sum
        return self.dfs(node.left, path_sum) + self.dfs(node.right, path_sum)
# Time, Space: O(n)

'''
 Path With Given Sequence (medium)
 LeetCode Premiem: Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
 https://medium.com/@yzhua3/leetcode-check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree-cb3012f5820
'''
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
    return dfs(root.left) or dfs(root.right)

