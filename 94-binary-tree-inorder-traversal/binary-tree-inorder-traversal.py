# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        lst = []
        self.inorder(root,lst)
        return lst
    def inorder(self,root,lst):
        if root is None:
            return
        self.inorder(root.left,lst)
        lst.append(root.val)
        self.inorder(root.right,lst)
