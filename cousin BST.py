class Treenode(object):
    def __init__(self,left=None,right=None,val=0):
        self.left=left
        self.right=right
        self.val=val
class Solution:
    def iscousiin(self,root,x,y):
        self.Depth_x=0      #Suru me depth  0 hai
        self.Depth_y=0          
        self.Parent_x=None  # aur parent none hai kyuki abhi hum root pe hain aur root ka koi parent nahi hai
        self.Parent_y=None
        def Traverse(node,parent,depth):    #hume 3 cheeze dekhni hain node ki val, parent kon hai, depth konsi hai
            if not node:
                return
            if node.val==x: #agar node ki val x ke equal hoti hai
                self.Depth_x=depth  #depth _x ki val depth k assign kar dete hain ya store kar lete hain
                self.Parent_x=parent    # isi tarah parent_x ki val parent ko assign kar dete hain
            if node.val==y:             # SAME -->
                self.Depth_y=depth      #       \|/
                self.Parent_y=parent
            Traverse(node.left,node,depth+1) 
            '''yaha traverse function ko  left aur right node ke liye call hota hai
              aur parent ki val current node ho jati hai like 1 - 2 par gaye to 2 ka parent hoga current node matlab 1
               aur har next node par depth ki value increse hogi '''
            Traverse(node.right,node,depth+1)
        Traverse(root,None,0)   #yaha traverse funtion call hota hai jaha cuurent parent None hai aur depth 0 hai
        return self.Depth_x==self.Depth_y and self.Parent_x!=self.Parent_y