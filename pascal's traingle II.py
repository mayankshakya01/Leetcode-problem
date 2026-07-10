class Solution:
    def getRow(self,rowindex):
        ans=[]
        row=0
        while row<=rowindex:
            if row==0:
                ans.append([1])
            if row>0:
                newrow=[1]
                prev=ans[row-1]
                for i in range(len(prev)-1):
                    mid=prev[i]+prev[i+1]
                    newrow.append(mid)
                newrow.append(1)
                ans.append(newrow)
            row+=1
        return ans[rowindex]