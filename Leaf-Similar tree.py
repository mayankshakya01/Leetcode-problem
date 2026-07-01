class Treenode(object):
    def __init__(self,left=None,right=None,val=0):
        self.left=left
        self.right=right
        self.val=val
class Solution(object):
    def leafSimilar(self,root1,root2):
        self.lst1=[]
        self.lst2=[]
        def traversal(node,lst):
            if not node:
                return 
            if not node.left and not node.right:
                lst.append(node.val)
            traversal(node.left,lst)
            traversal(node.right,lst)
        traversal(root1,self.lst1)
        traversal(root2,self.lst2)
        return self.lst1 ==self.lst2