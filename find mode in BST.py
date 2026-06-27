class Treenode(object):
    def __init__(self,left=None,right=None,val=0):
        self.left=left
        self.right=right
        self.val=val
class Solution(object):
    def findmode(self,root):
        self.count=0
        self.max_count=0
        self.pre=None
        self.result=[]
        def traverse(node):
            if not node:
                return 
            traverse(node.left)
            if self.pre is None:
                self.count=1
            elif self.pre== node.val:
                self.count+=1
            else:
                self.count=1
            if self.count>self.max_count:
                self.max_count=self.count
                self.result=[]
                self.result.append(node.val)
            elif self.count ==self.max_count:
                self.result.append(node.val)
            traverse(node.right)
        traverse(root)
        return self.result