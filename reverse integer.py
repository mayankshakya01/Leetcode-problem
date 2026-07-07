class Solution:
    def reverse(self,x):
        ans=0   #pahle hum ik ans variable banayenge jisme reverse integer ko store karenge
        sign =1     #fir hum sign ko declare karnge kyuki value + or -dono me ho sakti hai
        if x<0:     # agar value 0 se choti hai matlab mines me hai 
            sign=-1 # to sign ko -1 kar do kyuki kisi bhi value me -1 se multilpy karne par wo value bhi negative ho jati hai
        else:       # warna sign ko 1 rakho 
            sign=1
        x=abs(x)    #pahle hum value ko absolute value bana lenge
        while x>0:#fir ik loop jab tak x >0 hai
            digit=x%10  # digit me  x last value ko daal denge
            ans=ans*10+digit    # fir  ans me purni value me 10 se multiply karke  digit ko add kar denge
            x=x//10 # fir x ki value me se last digit ko hata denge 
        ans=ans*sign    # last me  ans me sign se multiply kar denge jisse value positive aur negative ho sakti hai
        if ans<-2**31 or ans>2**31-1:   # agar ans is range se bahar hota hai to 0 return kar denge
            return 0
        return ans