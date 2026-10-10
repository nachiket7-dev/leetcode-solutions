# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        count = 0
        return self.helper(root,count)
    def helper(self,root,count):
        if root is None:
            return count
        left = self.helper(root.left,count + 1)
        right = self.helper(root.right,count + 1)
        return max(left,right)

        