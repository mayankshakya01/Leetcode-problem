'''the question ->
Given an integer n, return all the structurally unique BST's (binary search trees), 
which has exactly n nodes of unique values from 1 to n.
 Return the answer in any order'''

class Treenode(object):
    def __init__(self,left=None,right=None,val=0):
        self.left=left
        self.right=right
        self.val=val
class Solution(object) :
    def genrateTree(self,n):
        def genrate(start,end):# number startfrom 1 and ends with n
            if start>end:           
                return [None]
            result=[]
            for node in range(start,end+1): # 1 to n range me ik loop chalayenge
                left=genrate(start,node-1)  #rule left subtree < root so left start from minimum and node-1 means if node ==1 then end on 1-1 yani ki left me 0 node hongi
                right=genrate(node+1,end)   # rule right subtree > root so right start from maximun means if node ==1 so right start with 1+1 yani ki right ki 2 node hongi
                for left_tree in left:      # fir left subtree pe ik loop
                    for right_tree in right:# and inner loop on right subtree for combine its value
                        root=Treenode(node)    #then create a new rootnode
                        root.left=left_tree     #left subtree ki value ko rootnode ke left me attach kar denge
                        root.right=right_tree   # right subtree ki value ko rootnode ke right me attach kar denge
                        result.append(root)     #result me root ki value ko add kar denge
            return result
        if n==0:
            return [None]
        return genrate(1,n)