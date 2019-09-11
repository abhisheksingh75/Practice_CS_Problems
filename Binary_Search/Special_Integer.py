"""
Given an array of integers A and an integer B, find and return the maximum value K such that there is no subarray in A of size K with sum of elements greater than B. 
Input Format
The first argument given is the integer array A.
The second argument given is integer B.
Output Format
Return the maximum value of K (sub array length).
Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9
1 <= B <= 10^9
For Example
Input 1:
    A = [1, 2, 3, 4, 5]
    B = 10
Output 1:
    2

Input 2:
    A = [5, 17, 100, 11]
    B = 130
Output 2:
    3
"""
def subarrayIsPossibe(A, K, B):
    sumOfSubArray = 0 
    N = len(A)
    #print("K:"+str(N-K+1))
    for i in range(N):
        #print(i)
        if i < K:
           sumOfSubArray += A[i]
           #print("sumOfSubArray"+str(sumOfSubArray))
        else:
            #print("sumOfSubArray"+str(sumOfSubArray))
            if sumOfSubArray <= B:
               sumOfSubArray += A[i]
               sumOfSubArray -= A[i-K]
            else:
                return False
    
    if sumOfSubArray <= B:
        return True
    else:
        return False



class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        first = 1
        last = len(A)
        ans = 0
        while(first<=last):
            mid = first + (last-first)//2
            if subarrayIsPossibe(A, mid, B) == True:
                ans = first
                first = mid+1
            else:
                last = mid-1
            #print(subarrayIsPossibe(A, mid,B))
        return last
