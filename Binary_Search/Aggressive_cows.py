"""
Farmer John has built a new long barn, with N stalls. Given an array of integers A of size N where each element of the array represents the location of the stall, and an integer B which represent the number of cows. His cows don't like this barn layout and become aggressive towards each other once put into a stall. To prevent the cows from hurting each other, John wants to assign the cows to the stalls, such that the minimum distance between any two of them is as large as possible. What is the largest minimum distance? 
Input Format
The first argument given is the integer array A.
The second argument given is the integer B.
Output Format
Return the largest minimum distance possible among the cows.
Constraints
2 <= N <= 100000
0 <= A[i] <= 10^9
2 <= B <= N
For Example
Input 1:
    A = [1, 2, 3, 4, 5]
    B = 3
Output 1:
    2

Input 2:
    A = [5, 17, 100, 11]
    B = 2
Output 2:
    95
   """
   
def ArrangeIsPossible(A,cows, min_diff):
    cows -= 1
    searchX = A[0]+min_diff
    
    for i in range(1,len(A)):
        if A[i] >= searchX:
            cows -= 1
            searchX = A[i] + min_diff
            if cows <= 0:
                return True
                break 
    if cows <= 0:
        return True
    else:
        return False
        
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        A.sort()
        max_diff, min_diff = 0, -1
        #calculate min_diff and max_diff
        for i in range(len(A)-1):
            diff = A[i+1] -A[i]
            min_diff = min(min_diff, diff)
        
        max_diff = A[len(A)-1] - A[0]+1
        
        low = min_diff
        high = max_diff
        
        while(high-low>1):
            mid = low + (high-low)//2
            #print("mid "+str(mid)+"ArrangeIsPossible "+str(ArrangeIsPossible(A, B, mid)))
            if (ArrangeIsPossible(A, B, mid) == True):
                low = mid
            else:
                high = mid
        
        return low            
            
            
            
            
