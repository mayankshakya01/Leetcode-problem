'''Question is -->
Given the root of a binary tree, return the sum of every tree node's tilt.
The tilt of a tree node is the absolute difference between the sum of all left subtree node values and all right subtree node values.
 If a node does not have a left child, then the sum of the left subtree node values is treated as 0. 
The rule is similar if the node does not have a right child.'''

class Solution:
    def __init__(self,left=None,right=None,val=0):
        self.left=left
        self.right=right
        self.val=val
    def findTilt(self,root):
        Total_Tilt=0
        def helper(node):       #we use a helper function for recursion
            if node is None:
                return 0
            left_sum=helper(node.left)  # here we get the sum of left subtree
            right_sum=helper(node.right)# here we get the sum of right subtree
            current_Tilt=abs(left_sum-right_sum)  #here we get absolute diffrence between left and right subtree
            Total_Tilt+=current_Tilt        # here we add tilt to total tilt
            return left_sum+right_sum+node.val    # inner function return the sum of subtree
        helper(root)        #here we call the inner function 
        return Total_Tilt