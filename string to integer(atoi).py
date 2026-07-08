'''Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.'''

 

class Solution:
    def stringTointeger(self,s):
        ans=0
        sign=1
        i=0
        while i <len(s) and s[i]==" ":  #agar space hai to next character pe jaao
            i+=1
        if i<len(s) and s[i]=="-":  # agar  string me - diya hai to sign ko -1 kar do
            sign=-1
            i+=1
        if i<len(s) and s[i]=="+":
            i+=1
        while i<len(s)and s[i].isdigit():   #agar string me digit hain to ->
            ans=ans*10+int(s[i])        # ans me daal do
            i+=1                        #aur i ko next character par bhej do 
        ans=ans*sign
        if ans> 2**31-1:    # agar ans isse bada aata hai to ye return kardo
            return 2**31-1
        if ans<-2**31:
            return -2**31
        return ans