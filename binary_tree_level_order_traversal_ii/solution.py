"""
Given a binary tree, return the bottom-up level order traversal of its nodes'
values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree {3,9,20,#,#,15,7},
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        stack = []
        if root is None:
            return stack
        queue = []
        level = []
        queue.append(root)
        queue.append(None)
        while queue:
            root = queue.pop(0)
            if root is None:
                stack.append(level[:])
                level = []
                if queue:
                    queue.append(None)
            else:
                level.append(root.val)
                if root.left is not None:
                    queue.append(root.left)
                if root.right is not None:
                    queue.append(root.right)
        res = []
        while stack:
            res.append(stack.pop())
        return res
