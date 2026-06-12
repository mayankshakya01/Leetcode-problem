# class Solution:
#     def height(self,root):
#         if root is None:
#             return 0
#         return 1+max(self.height(root.left), self.height(root.right))
#     def isBalanced(self,root):
#         if root is None:
#             return True
#         left_height=self.height(root.left)
#         right_height=self.height(root.right)
#         current=abs(left_height-right_height)
#         if current>1:
#             return False
#         return self.isBalanced(root.left)and self.isBalanced(root.right)


