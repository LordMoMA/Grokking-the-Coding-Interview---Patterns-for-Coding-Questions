'''
102. Binary Tree Level Order Traversal

https://leetcode.com/problems/binary-tree-level-order-traversal/description/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            curLevel = []
            for _ in range(levelSize):
                cur = queue.popleft()
                curLevel.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(curLevel)
        return res
# time, space O(n)


'''
107. Binary Tree Level Order Traversal II
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/

Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
'''
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = deque()
        if not root:
            return res
        queue = deque()
        queue.append(root)
        while queue:
            curLevel = []
            levelSize = len(queue)
            for _ in range(levelSize):
                cur = queue.popleft()
                curLevel.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.appendleft(curLevel)
        return res
# time, space O(n)


'''
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        leftToRight = True
        queue = deque()
        queue.append(root)

        while queue:
            curLevel = deque()
            levelSize = len(queue)
            for _ in range(levelSize):
                cur = queue.popleft()

                if leftToRight:
                    curLevel.append(cur.val)
                else:
                    curLevel.appendleft(cur.val)

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(list(curLevel))
            leftToRight = not leftToRight
        return res
# time, space O(n)


'''
637. Average of Levels in Binary Tree

https://leetcode.com/problems/average-of-levels-in-binary-tree/
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if not root:
            return res

        queue = deque()
        queue.append(root)

        while queue:
            curLevel = []
            levelSize = len(queue)
            for _ in range(levelSize):
                cur = queue.popleft()
                curLevel.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            levelAverage = sum(curLevel) / levelSize
            res.append(levelAverage)
        return res

# solution 2


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        if not root:
            return res

        queue = deque()
        queue.append(root)

        while queue:
            curLevel = []
            levelSize = len(queue)
            levelSum = 0
            for _ in range(levelSize):
                cur = queue.popleft()
                curLevel.append(cur.val)
                levelSum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            levelAverage = levelSum / levelSize
            res.append(levelAverage)
        return res
# time, space O(n)
