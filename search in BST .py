class Treenode(object):
    def __init__(self,left=None,right=None,val=0):
        self.left=left
        self.right=right
        self.val=val
class Solution(object):
    def searchBST(self,root,val):
        def search(node):
            if not node:
                return 
            if node.val==val:   # agar node ki val ,val ke equal ho to node return kar do
                return node
            left=search(node.left)
            if left:            # agar val left me ho to left subtree return kar do
                return left
            right=search(node.right)    #agar val right me ho to right subtree return kar do
            if right:
                return right
        return search(root)
    
'''                             OR                              '''
class Solution(object):             #ye code fast hai kyuki isme dono taraf val ko search nahi karna padta hai
    def searchBST(self,root,val):
        if root is None or root.val ==val:  #agar root none ho to none return kar do aur agar root i val ,val ke equal hoo to root return kar do
            return root
        if val<root.val:        #agar val root ki val se choti ho to kyuki BST ka rule hai left < root < right
            return self.searchBST(root.left,val)    #left me search karo 
        return self.searchBST(root.right,val)   # warna right me search karo