class Treenode(object):
    def __init__(self,left=None,right=None,val=0):
        self.left=left
        self.right=right
        self.val=val
class Solution(object):
    def findsubtree(self,root,Subroot):
        def findsubroot(node):
            if node is None:
                return False
            if issame(node,Subroot):
                return True
            return findsubroot(node.left) or findsubroot(node.right)
        def issame(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val!=q.val:
                return False
            return issame(p.left,q.left) and issame(p.right,q.right)
        return findsubroot(root)