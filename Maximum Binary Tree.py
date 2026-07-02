class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution(object):
    def maxbinarytree(self,nums):
        def visit(node):
            if not node:
                return None
            maximum=max(node)   #first we find the maximum val of the nums
            idx=node.index(maximum) #aur uske baad jo maximum val mili thi ab uskaindex find karnge

            dummy=TreeNode(maximum)     #fir us maximum val ko dummy node ka root bana denge
            dummy.left=visit(node[:idx])    # fir visit function ko left node ke liye fir call karnge jo start se lekar maximum ke index tak chalege
            dummy.right=visit(node[idx+1:]) # fir visit ko right node keliye call karenge  
            return dummy
        return visit(nums)