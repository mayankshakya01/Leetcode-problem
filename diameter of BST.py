class Treenode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def DiameterBST(self,root):
        self.diameter=0
        def height(node):
            if node is None:
                return 0
            left=height(node.left)
            right=height(node.right)
            self.diameter=max(self.diameter,left+right)
            return max(left,right)+1
        height(root)
        return self.diameter