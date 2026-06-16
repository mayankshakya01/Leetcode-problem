class Solution:
    def __init__(self,left=None,right=None,val=0):
        self.left=left
        self.right=right
        self.val=val
    def sumpath(self,root,target):
        paths=[]
        if root is None:
            return[]
        if root.left is None and root.right is None:
            if root.val== target:
                return [[root.val]]
            else:
                return[]
        left_path=self.sumpath(root.left,target-root.val)
        for path in left_path:
            paths.append([root.val]+path)
        right_path=self.sumpath(root.right,target-root.val)
        for path in right_path:
            paths.append([root.val]+path)
        return paths

obj=Solution()
print(obj.sumpath([5,4,8,11,None,13,4,7,2,None,None,5,1],22))