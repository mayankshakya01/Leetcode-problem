class Treenode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def findSecondvalue(self,root):
        self.minimum=[]
        def findminimum(node):
            if not node:
                return 
            self.minimum.append(node.val)
            findminimum(node.left)
            findminimum(node.right)
        findminimum(root)       #function call
        value=sorted(set(self.minimum)) #pahle value ko set me convert karo fir use sort kar do
        if len(value)<2:        #agar values ki len 2 se kam ho to -1 return kr do
            return -1
        return value[1]         #nahi to value me 1 index wali value return kar do