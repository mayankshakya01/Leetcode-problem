class Solution :
    def genrate(self,numRows):
        ans=[]  #pahle ik empty list bana lenge
        row=0   # fir row ko define kar denge kyuki pascal'traingle me rows bhi hoti hain
        if numRows==1:  # agar user ne numRows 1 diya ho to list me ik aue list bana ke 1 return kar do
            return [[1]]
        while row<numRows:  # jab tak row numrows se choti hai kyuki row 0 se start ho rahi hai
            if row==0:  # agar row 0 hai to ans me append kar do 1 kyuki uska koi prev nahi hai
                ans.append([1])
            if row>0:   # agar row 0 se badi  hai to 
                newrow=[1]  # newrow name ka ik variable banao jisme pahla element hamesa 1 hoga
                prev=ans[row-1] # fir prev ko define karo -> prev kisi ans list me current row -1  matlab pichli ans list 
                for num in range(len(prev)-1):  # fir ik loop len(prev)-1 tak kyuki hum prev element ko add karenge warna jab num+1 hoga to out or range ho jayega
                    mid=prev[num]+prev[num+1]   # fir prev ke num  aur num +1 ko add karke mid me daal denge 
                    newrow.append(mid)# fir newrow me mid ko append kar denge
                newrow.append(1)    # newrow me 1 ko append kar denge kyuki newroe ka last element hamesha 1 hoga
                ans.append(newrow)  # fir newrow jo ik list hai usko ans me append kar denge
            row+=1  # aur har baar row ko update karenge
        return ans