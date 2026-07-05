class Solution:
    def longestString(self,s):
        long=""
        for i in range(len(s)):
            original=""
            for j in range(i,len(s)):
                original=s[j]
                if original==original[::-1]:    #check karnge ki origianl ka reverse origianl ke equal hota hai
                    if len(original)>len(long):# agar hai to fir check karo ki original ki len purane palandromic string se badi hai 
                        long=original           # agar hai to long me new palandromic string ko dal do jo original me hai 
        return long         # sabse long palandromic string ko return kar do