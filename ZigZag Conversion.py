class Solution:
    def convert(self,s,numrows):
        if numrows==1:  #agar numsrow 1 hui to wahi string return kar do
            return s
        rows=[""]*numrows   #hum ik list ke ander empty row banayenge aur usko numrows se multiply kar denge jisse numrows jtni empty sting ban jayengi
        direction=1     # fir hum direction set karnge 1 for down and -1 for up(user defined)
        currentrow=0    #har bar row ko change karna padega
        for ch in s:
            rows[currentrow]+=ch    #pahle character ko add karnge
            if currentrow==0:   # fir check karnge agar currentrow 0 par ho to uska direction 1 (down )kar do 
                direction=1
            elif currentrow==numrows-1: #agar currentrow last row pe ho to uska direction -1(up)kar do
                direction=-1
            currentrow+=direction   #currentrow ko har bar update karo 
        return "".join(rows)    #sabhi string ko join karke return kar do
