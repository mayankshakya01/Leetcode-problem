class Treenode(object):
    def __init__(self,left=None,right=None,val=0):
        self.left=left
        self.right=right
        self.val=val
'''                                     with the help of recursive call                                         '''
class Solution(object):
    def getTargetCopy(self,original,cloned,target):
        def traverse(original_node,cloned_node):    #hum dono trees(original,cloned) par ik sath traverse karenge
            if not original_node:                   
                return None
            if original_node==target:               #agar original tree target equal ho jata hai to cloned tree ki same positon return kar do
                return cloned_node                  # kyuki hum dono tree pe ik sath travese kar rahe hain to same position milegi
            left=traverse(original_node.left,cloned_node.left)
            if left:                                # agar target left me mile to left node ki position return kar do
                return left
            right=traverse(original_node.right,cloned_node.right)
            if right:                               # agar target right me mile to right node ki position return kar do
                return right
        return traverse(original,cloned)        #last me hum hum dono tree ko ik sath call karenge
    
'''                                     with the help of queue                                                  '''

from collections import deque
class Solution (object):
    def getTargetCopy(self,original,cloned,target):
        queue=deque([(original,cloned)])    #hum original aur cloned tree ko tuple ki form me queue me dal denge.
        '''tuple form me is liye dal rae hain kykui hume dono tree ko ik sath hi track(dekhna)hai. agar tuple nahi banayenge
        to pairing toot jayegi aur original aur cloned dono alag alag item ban jayengea aur pata nahi chalege ki kon sa original hai
        aur kon cloned'''
        while queue:
            ori_node,clo_node=queue.popleft()   #dono tree ki element ko ik sath queue se nikalenge
            if ori_node ==target:   # agar  original tree target ke equal hoti hai to cloned tree ki same position return kar do
                return clo_node
            if ori_node.left:       #original tree ke left side visit karo agar koi node hai to usko queue me append kar do
                queue.append((ori_node.left,clo_node.left))
            if ori_node.right:
                queue.append((ori_node.right,clo_node.right))
        return None