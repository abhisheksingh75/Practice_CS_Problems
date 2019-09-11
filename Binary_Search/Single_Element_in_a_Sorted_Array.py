"""
Given a sorted array of integers A where every element appears twice except for one element which appears once, find and return this single element that appears only once. 
Input Format
The only argument given is the integer array A.
Output Format
Return the single element that appears only once.
Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9 
For Example
Input 1:
    A = [1, 1, 2, 2, 3]
Output 1:
    3

Input 2:
    A = [5, 11, 11, 100, 100]
Output 2:
    5
"""
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        first = 0
        last = len(A)-1
        while(first <=last):
            mid = first + (last-first)//2
            
            if first == last :
                return A[first]
            
            if mid%2 == 0:
                
                if mid+1 < len(A) and  A[mid] == A[mid+1]:
                    first = mid +2 
                else:
                    last = mid
            else:
                
                if mid-1 > -1 and  A[mid] == A[mid-1]:
                    first = mid + 1
                else:
                    last = mid -1
