class Solution(object):
    def __init__(self,val=None,children=None):
        self.val=val
        self.children=children

    def preorder(self,root):
        value=[]        #we created an empty list named value
        if root is None:
            return 
        value.append(root.val)  # firstly we append the root node in list

        '''self.children is used in N -ary tree because in this tree there is no left and right pointer.
        and insted  self.children is store all the nodes value as a list '''

        for node in root.children:  #   here we use an loop to go each element of children list
            '''here we use extend keyword insted of append because append add all object as a single elemnet but extend add element seperatorly'''
            value.extend(self.preorder(node))
        return value