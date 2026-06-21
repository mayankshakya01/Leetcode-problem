class Solution(object):
    def __init__(self,val=None,children=None):
        self.val=val
        self.children=children
    def postorder(self,root):
        value=[]
        if not root:
            return 
        for node in root.children:
            value.extend(self.postorder(node))
        value.append(root.val)
        return value