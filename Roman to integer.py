class Solution:
    def Romantointeger(self,roman):
        dic={
            "M":1000,
            "D":500,
            "C":100,
            "L":50,
            "X":10,
            "V":5,
            "I":1
        }
        result=0
        for num in range(len(roman)):
            if num+1<len(roman) and dic[roman[num]] <dic[roman[num+1]]:
                result-=dic[roman[num]]
            else:
                result+=dic[roman[num]]
        return result

obj=Solution()
print(obj.Romantointeger("VII"))