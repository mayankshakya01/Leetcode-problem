class Treenode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def increseorder(self,root):
        dummy=Treenode(0)   #jab ik nayi node banani padti hai to hum ik duumy node bana lete hain
        self.prev=dummy     #yaha prev dummy ko point kar raha hai
        def increse(node):
            if not node :
                return 
            increse(node.left)
            self.prev.right=node    #yaha pe left me leaf node se pahle wale node ko leaf ke right me jod denge
            node.left=None      #aur us node ki left node ko None kr denge
            self.prev=node      #fir us jodi gayi prev node ko current node bana denge
            increse(node.right)
        increse(root)
        return dummy.right      #yaha dummy node ka right node return kar denge