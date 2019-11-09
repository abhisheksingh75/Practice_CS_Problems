"""
Given an integer A, we call k >= 2 a good base of A, if all digits of A base k are 1. Now given a string representing A, you should return the smallest good base of A in string format. 
Input Format
The only argument given is the string representing A.
Output Format
Return the smallest good base of A in string format.
Constraints
3 <= A <= 10^18
For Example
Input 1:
    A = "13"
Output 1:
    "3"     (13 in base 3 is 111)

Input 2:
    A = "4681"
Output 2:
    "8"     (4681 in base 8 is 11111).
   """
    # @param A : string
    # @return a strings
    def solve(self, A):
        A = int(A)
        #find smallest m with highest number of bits set, so starting from maximum no of bits        
        for i in range(64, -1, -1):
            #print("i->"+str(i))
            low = 2
            high = A
            while(high-low > 1):
                mid = low + (high-low)//2
                sum = (((mid**i)-1)//(mid-1))   #geometric sum of 1+m+m2+m3+...mi
                #print("mid :"+str(mid)+"sum "+str(sum))
                if sum == A:
                    #print("alpha")
                    return mid
                elif sum > A:
                    #print("beta")
                    high = mid
                else:
                    #print("gamma")
                    low = mid
        
        return low    
