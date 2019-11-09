"""
Ath Magical Number
Given three positive integers A, B and C. A positive integer is magical if it is divisible by either A or B. Return the A-th magical number. Since the answer may be very large, return it modulo 109 + 7. 
Input Format
The first argument given is an integer A.
The second argument given is an integer B.
The third argument given is an integer C.
Output Format
Return the A-th magical number modulo (10^9+7).
Constraints
1 <= A <= 10^9
2 <= B, C <= 40000 
For Example
Input 1:
    A = 1
    B = 2
    C = 3
Output 1:
    2
    Explanation 1:
        1st magical number is 2.

Input 2:
    A = 4
    B = 2
    C = 3
Output 2:
    6
   """

def gcd(x,y):
    x,y = max(x,y), min(x,y)
    while(y>0):
        x,y = y,x%y
    return x
    
def nthnumber(mid, LCM, A,B):
    return mid//A + mid//B - mid//LCM
    
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, N,A,B):
        
        LCM = (A*B)//gcd(A,B)
        first = 0 
        last = (10**18+7)
        ans = 0
        while(first<=last):
            mid = (first+last)//2
            #print("first:"+str(first)+"last:"+str(last)+"mid:"+str(mid)+"nthnumber(mid, LCM, A,B):"+str(nthnumber(mid, LCM, A,B)))
            if nthnumber(mid, LCM, A,B) == N:
                ans =  mid
                last = mid-1
            elif nthnumber(mid, LCM, A,B) > N:
                last = mid - 1
            else:
                first = mid + 1
        return ans%(10**9+7)
