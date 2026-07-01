from collections import deque
class Treenode(object):
    def __init__(self,left=None,right=None,val=0):
        self.left=left
        self.right=right
        self.val=val
class Solution(object):
    def average(self,root):
        queue=deque()   #pahle hum ik queue banate hain
        queue.append(root) # fir us queue me root ki value ko append kar dete hain kyuki uska level 0 hai to wo akela hoga
        result=[]       # yaha hum average ko store karnge
        while queue:    #fir ik while loop chalaenge jab tak queue hai
            size=len(queue) # har baar queue ka size calculate karnge
            level_sum=0     #fir us level ki sabhi val ko level_sum name ke variable me add kar dange
            for level in range(size):   # fir ik loop chalenge  us level par  queue ke size tak 
                node=queue.popleft()    # fir hum queue me store value ko pop(nikal) kar denge aur usko node name ke variable me store kar denge
                level_sum+=node.val     # fir level_sum me us node ki sabhi value ko add ka denge
                if node.left:                # agar us node ka koi left child hai
                    queue.append(node.left)     # to uski val ko queue ke dal do
                if node.right:               #same
                    queue.append(node.right)
            result.append(float(level_sum)/size)    #level_sum ki val ko us queue ke size se divid kar do aur usko result me append kar do kyuki average=val/number_of val
        return result
    

