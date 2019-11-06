

def calcSPF(SPF):
    len_of_SPF  = len(SPF)
    SPF = [i for i  in range(len_of_SPF)]
    #print(SPF)
    for i in range(2, floor(sqrt(len_of_SPF))+1, 1):
        if SPF[i] >= i:
            for j in range(i, len_of_SPF, i):
                if SPF[j] >= j:
                    SPF[j] = i 
    return SPF
from math import floor, sqrt
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        max_no = 0
        for i in range(len(A)):
            max_no = max(max_no, A[i])
        #print(max_no)    
        #smallest prime factor
        SPF = [-1]*(max_no+1)
        len_of_A = len(A)
        return_list = [0]*len_of_A
        #find SPF of all all possible values of A
        SPF[1] = 1
        SPF = calcSPF(SPF)
        for i in range(0, len_of_A, 1):
            no_of_divisor = 1
            while(A[i] > 1):
                prime_no = SPF[A[i]] 
                count = 0
                while(A[i]%prime_no == 0):
                    #print("SDcdc")
                    count += 1
                    A[i] = A[i]//prime_no
                no_of_divisor *= (count + 1)
            #print(no_of_divisor)
            return_list[i] = no_of_divisor
            
        return return_list
            
            
            
 
