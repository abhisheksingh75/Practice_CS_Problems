"""
Given an array of integers A. If i < j and A[i] > A[j] then the pair (i, j) is called an inversion of A. Find the total number of inversions of A modulo (10^9 + 7). 
Input Format
The only argument given is the integer array A.
Output Format
Return the number of inversions of A modulo (10^9 + 7).
Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9 
For Example
Input 1:
    A = [1, 2, 5, 4, 3]
Output 1:
    3

Input 2:
    A = [5, 17, 100, 11]
Output 2:
    1
    """
    
def recurMergeSort(A,left, right):
    inv_Count = 0
    if left < right:
        mid  = (left + right)>>1
        inv_Count += recurMergeSort(A,left, mid)
        inv_Count += recurMergeSort(A,mid+1, right)
        inv_Count += merge(A,left, mid, right)
    return inv_Count

def merge(A,left_indx, mid_indx, right_indx):
    rev_Count = 0
    i = 0
    j = 0
    k = left_indx
    left = A[left_indx:mid_indx+1]
    n = mid_indx-left_indx+1
    right = A[mid_indx+1:right_indx+1]
    m = right_indx-mid_indx
    while(i<n and j<m):
        if left[i]<=right[j]:
            A[k] = left[i]
            i += 1
            k += 1
        else:
            rev_Count += (n-i) 
            A[k] = right[j]
            j += 1
            k += 1
            
    while(i<n):
        A[k] = left[i]
        i += 1
        k += 1      
    while(j<m):
        A[k] = right[j]
        j += 1
        k += 1  
    return rev_Count  


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        count = 0
        count  = recurMergeSort(A,0, len(A)-1)
        return count%(10**9+7)
