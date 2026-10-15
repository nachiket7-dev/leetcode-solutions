# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        l1 = []
        l2 = []
        self.inorder(p,l1)
        self.inorder(q,l2)
        if len(l1) != len(l2):
            return False
        for i in range(len(l1)):
            if l1[i] != l2[i]:
                return False
        return True
    def inorder(self,root,lst):
        if root is None:
            lst.append(None)
            return 
        lst.append(root.val)
        self.inorder(root.left,lst)
        self.inorder(root.right,lst)
        