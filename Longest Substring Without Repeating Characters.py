class Solution:
    def longestsubstring(self,s):
        maxlen=0        #pahle hum ik variable bana lenge jo len store karege kyuki len hi puchi gayi hai
        for i in range(len(s)): #fir ik loop chalaenge 
            string=""           # fir uske ander ik variablr banayenge jo string character ko store karega aur her bar string empty ho jaye taki keval ik character check ho sake
                                #warna mulptiple character check honge
            for j in range(i,len(s)):   #fir ik loop j chalayenge
                if s[j] not in string:  #fir check karnge ki s[j]means j index ka character string me ahi ya nahi
                    string+=s[j]        #agar nahi hai to usko  string me add kar do
                    maxlen=max(maxlen,len(string))  # fir string ki len nikal lo aur usko maxlen me store kar do
                else:                   #agar character repeat hota hai to brak kar jaao
                    break
        return maxlen
    