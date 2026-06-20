class Solution:
    def __init__(self,left=None,right=None,val=0):
        self.left=left
        self.right=right
        self.val=val
    '''this work but it time complxity is O((log n)^2) but we need less then (O(n))'''
    # def Count(self,root):
    #     if not root:
    #         return 0
    #     left=self.Count(root.left)
    #     right=self.Count(root.right)
    #     return 1+left+right

    def CountNodes(self,root):
        def height(node):
            h=0
            while node:
                h+=1
                node=node.left
            return h
        left=height(root.left)
        right=height(root.right)
        '''here "<< is left shift operator " 1<<left means 1 ko left time left shift kar do
        like 1<<3 likha hai toh iska matlab hai 0001 ko 1000 kkar do means 1 ko 3 position left shift kar do'''
        if left == right:
            return (1<<left)+self.CountNodes(root.right)
        else:
            return(1<<right)+self.CountNodes(root.left)