class Solution:
    def Twosum(self,nums,target):
        num=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]

obj=Solution()
obj.Twosum([2,4,5,7],9)