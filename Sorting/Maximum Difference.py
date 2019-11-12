"""
Given an array of integers A and an integer B. Find and return the maximum value of | s1 - s2 | where s1 = sum of any subset of size B, s2 = sum of elements of A - sum of elemets of s1 Note |x| denotes the absolute value of x. 
Input Format
The arguments given are the integer array A and integer B.
Output Format
Return the maximum value of | s1 - s2 |.
Constraints
1 <= B < length of the array <= 100000
1 <= A[i] <= 10^5 
For Example
Input 1:
    A = [1, 2, 3, 4, 5]
    B = 2
Output 1:
    9

Input 2:
    A = [5, 17, 100, 11]
    B = 3
Output 2:
    123
    """
    class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        s1,sum,s2 = 0, 0, 0
        #print(A)
        if B < len(A)//2:
            for i in range(len(A)):
                if i<B:
                    s1 += A[i]
                sum +=A[i] 
            s2 = sum - s1
        else:
            count = 0
            for i in range(len(A)-1, -1, -1):
                if count<=B-1:
                    s1 += A[i]
                    count += 1
                sum +=A[i] 
            s2 = sum - s1
        #print("sum:"+str(sum)+"s1:"+str(s1)+"s2:"+str(s2))    
        return abs(s1-s2)
