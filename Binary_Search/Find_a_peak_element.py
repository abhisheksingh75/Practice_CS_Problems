"""
Given an array of integers A, find and return the peak element in it. An array element is peak if it is NOT smaller than its neighbors. For corner elements, we need to consider only one neighbor. For example, for input array {5, 10, 20, 15}, 20 is the only peak element. Following corner cases give better idea about the problem.
1) If input array is sorted in strictly increasing order, the last element is always a peak element. 
For example, 5 is peak element in {1, 2, 3, 4, 5}.
2) If input array is sorted in strictly decreasing order, the first element is always a peak element. 
10 is the peak element in {10, 9, 8, 7, 6}.
Note: It is guranteed that the answer is unique. 
Input Format
The only argument given is the integer array A.
Output Format
Return the peak element.
Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9 
For Example
Input 1:
    A = [1, 2, 3, 4, 5]
Output 1:
    5

Input 2:
    A = [5, 17, 100, 11]
Output 2:
    100
   """
   class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        first = 0
        last = len(A)-1
        
        while(first<=last):
            mid = first + (last-first)//2
            if(mid == 0 or mid  == N-1 or (A[mid] > A[mid-1] and A[mid] > A[mid+1])):
                return A[mid]
            elif A[mid-1] >= A[mid]:
                last = mid-1
            elif A[mid+1] >= A[mid]:
                first = mid + 1
        
