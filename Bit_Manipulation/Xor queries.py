"""
Xor queries
You are given an array (containing only 0 and 1) as element of N length. Given L and R, you need to determine value of XOR of all elements from L to R (both inclusive) and number of unset bits (0's) in the given range of the array. Input
First argument contains the array of size N containing 0 and 1 only (1<=N<=100000). 

Second argument contains a 2D array with Q rows and 2 columns, each row represent a query with 2 columns representing L and R. 

(1<=Q<=100000), (1<=L<=R<=N).
Output
Return an 2D array of Q rows and 2 columns i.e the xor value and number of unset bits in that range respectively for each query.
Examples Input
1 0 0 0 1
2 4
1 5 
3 5
Output
0 3
0 3
1 2
Explanation Testcase 1-
In the given case the bit sequence is of length 5 and the sequence is 1 0 0 0 1. For query 1 the range is (2,4), and the answer is (array[2] xor array[3] xor array[4]) = 0, and number of zeroes are 3, so output is 0 3. Similarly for other queries.
"""
class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        lenofA = len(A)
        prefixSum = [0]*lenofA
        noOfZeors = 0
        rangelen = 0
        return_list = [[0 for i in range(2)] for i in range(len(B))]
        if A[0] == 0:
            prefixSum[0] = 1
        
        for i in range(1, lenofA, 1):
            if A[i] == 0:
               prefixSum[i] = 1 + prefixSum[i-1]
            else:
                prefixSum[i] =  prefixSum[i-1]
        
        for i in range(len(B)):
            start, end  = B[i][0]-1, B[i][1]-1
            if start-1 >= 0:
                noOfZeors = prefixSum[end]-prefixSum[start-1]
            else:
                noOfZeors = prefixSum[end]
            rangelen = (end-start+1)-noOfZeors
            if  rangelen%2 == 0:
                return_list[i][0] = 0
            else:
                return_list[i][0] = 1
            #print("noOfZeors"+str(noOfZeors))
            return_list[i][1] = noOfZeors
        return return_list 
                    
            
            
