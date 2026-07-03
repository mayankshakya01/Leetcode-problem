class ListNode(object):
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class Solution(object):
    def addTwoNumbers(self,l1,l2):
        dummy=ListNode(0)   #pahle hum ik dummy list banayenge
        current=dummy
        carry=0         # ik carry  banayenge
        while l1 or l2 or carry:    #fir ik loop chalaenge jab tak l1 ya l2 ya carry bachi hai
            '''listNode me node hain par hume integer ko jodna hai'''
            x=l1.val if l1 else 0   #  agar l1 me val hai to usko x me store kar do warna 0 store kar do kyuki dono node same length ki honi chahiye
                                    #kyuki  agar ik node nahi hui to add karna namumkin hai kuyki add karne ke liye value hi nahi hogi isliye waha 0 store kiya hai 
            y=l2.val if l2 else 0   #same  for l2

            total=x+y+carry # ab dono list ki value aur carry(agar ho to ) add kar do
            carry=total//10 #fir check karngeki add ki gayi value me carry hai ya nahi
            
            current.next=ListNode(total%10) #fir dummy list me (total%10) ko store karenge kyuki agar value 11  ya usse jayda hui to carry hogi 1 to 1 store hona chahiye 
            current=current.next    # fir har bar list ko agle node par move kar denge
        return dummy.next   # fir dummy.next ko print kara denge kyuki list agle node se start hogi