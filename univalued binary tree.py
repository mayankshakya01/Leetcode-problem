'''A binary tree is uni-valued if every node in the tree has the same value.

Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.

'''
import shutil
shutil.move("local/univalued binary tree.py","Leetcode-problem/univalued binary tree.py")
class Solution :
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    def univalued(self,root):
        value=root.val
        def checker(node):
            if not node:
                return True
            if node.val==value:
                return True
            return checker(node.left)and checker(node.right)
        return checker(root)