class Solution:
    def invert(self,root):
        if root is None:
            return root
        left_side=self.invert(root.left)
        right_side=self.invert(root.right)
        left_side,right_side=right_side,left_side
        return root