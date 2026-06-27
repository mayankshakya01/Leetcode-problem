class Treenode(object):
    def __init__(self,val=None,children=None):
        self.val=val
        self.children=children
class Solution(object):
    def maxDepth(self,root):
        Depth=[]
        if not root :
            return 
        if not root.children:
            return 1
        for child in root.children:     #yaha hum children me ik loop chalayenge
            Depth.append(self.maxDepth(child))  #har node ke liye maxDepth function ko call karnge aur usko Depth list me append kar denge
        return max(Depth)+1