# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        q = collections.deque([root])
        # q.append(root)
        # visited = []
        while q:
            temp = q.popleft()
            if temp :
                temp.left, temp.right = temp.right, temp.left
                q.append(temp.left)
                q.append(temp.right)
        return root
        