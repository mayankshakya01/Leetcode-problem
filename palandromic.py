# import shutil
# shutil.move("my-first-repository\palandromic.py","leetcode-problem")

class Solution:
    def ispalandromic(self,num):
        reverse=0
        orignal=num
        while num>0:
            tmp=num%10
            reverse=reverse*10+tmp
            num=num//10
        return reverse== orignal
obj=Solution()
print(obj.ispalandromic(121))