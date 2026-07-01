class Treenode(object):
    def __init__(self,left=None,right=None,val=0):
        self.left=left
        self.right=right
        self.val=val
'''                             root1 ko hi modify karke return kar do              (best)      '''
class Solution(object):
    def meargeBinarytree(self,root1,root2):
        def traverse(r1,r2):    #dono trees pe ik sath visit karnge
            if not r1:          # agar root 1 nahi hai to to root2 ko return kar do
                return r2
            if not r2:
                return r1
            r1.val=r1.val+r2.val    #root1 me root 2 ki value ko add kar do taki merged tree ban sake aur root1 ko return kar do
            traverse(r1.left,r2.left)
            traverse(r1.right,r2.right)
            return r1
        return traverse(root1,root2)
    
