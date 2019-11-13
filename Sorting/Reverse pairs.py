"""
Given an array of integers A, we call (i, j) an important reverse pair if i < j and A[i] > 2*A[j]. Return the number of important reverse pairs in the given array A. 
Input Format
The only argument given is the integer array A.
Output Format
Return the number of important reverse pairs in the given array A.
Constraints
1 <= length of the array <= 100000
1 <= A[i] <= 10^9 
For Example
Input 1:
    A = [1, 3, 2, 3, 1]
Output 1:
    2

Input 2:
    A = [2, 4, 3, 5, 1]
Output 2:
    3
   """
   
def recurMergeSort(A, tmp_array, left, right):
    inv_Count = 0
    if left < right:
        mid  = (left + right)//2
        inv_Count += recurMergeSort(A, tmp_array, left, mid)
        inv_Count += recurMergeSort(A, tmp_array, mid+1, right)
        inv_Count += merge2(A, left, mid, right)
        #print(A)
    return inv_Count
 

def merge2(A,left_indx, mid_indx, right_indx):
    rev_Count = 0
    i = 0
    j = 0
    k = left_indx
    left = A[left_indx:mid_indx+1]
    n = mid_indx-left_indx+1
    right = A[mid_indx+1:right_indx+1]
    m = right_indx-mid_indx

    #logic to calculate inversion count
    while(i<n and j<m):
        if left[i]<=2*right[j]:
            i += 1
        else:
            rev_Count += (n-i) 
            j += 1
            
    i, j= 0,0
    while(i<n and j<m):
        if left[i]<=right[j]:
            A[k] = left[i]
            i += 1
            k += 1
        else:
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
        temp_Array = [0]*len(A)
        count =  recurMergeSort(A,temp_Array, 0, len(A)-1)
        #print(A)
        return count%(10**9+7)
        
