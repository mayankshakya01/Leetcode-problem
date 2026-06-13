class Treenode(object):
    def __init__(self,left=None,right=None,val=0):
        self.val=val
        self.left=left
        self.right=right
class Solution:
    def isSum(self,root,target):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val== target
        return self.isSum(root.left,target-root.val)or self.isSum(root.right,target-root.val)
obj =Solution()
print(obj.isSum([5,4,8,11,None,13,4,7,2,None,None,None,1], target = 22))