import math
def nCr(n, k):
    
    return math.factorial(n)//((math.factorial(n-k))*(math.factorial(k)))
    
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        B.sort()
        #aux_a will store no of elements in each gap and way to make move in that group if group is isolated
        AUX_A = [[ 0 for i in range(2) ] for i in range(len(B)+1)]
        
        for i in range(len(AUX_A)):
            if i == 0:
                #populate first group 
                AUX_A[i][0] = B[i]-1
                AUX_A[i][1] = 1
            elif i == len(AUX_A)-1:
                #popualte last group 
                AUX_A[i][0] = A- B[i-1]
                AUX_A[i][1] = 1
            else:
                #populate for in between groups
                AUX_A[i][0] = B[i]-B[i-1]-1
                AUX_A[i][1] = int(2**(AUX_A[i][0]-1))
        #print(B)
        #print(AUX_A)
        prev_count = 0
        ans = 1
        for i in range(len(AUX_A)):
            if AUX_A[i][0] == 0:
                continue
            prev_count += AUX_A[i][0]
            #print(str(AUX_A[i][1]))
            ans *= (AUX_A[i][1]*nCr(prev_count, AUX_A[i][0]))
            #print("ans:"+str(ans))
        
        return ans%(10**9+7)
            
                
        
