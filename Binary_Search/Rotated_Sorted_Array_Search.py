"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand. (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2 ). You are given a target value to search. If found in the array, return its index, otherwise return -1. You may assume no duplicate exists in the array.
Input : [4 5 6 7 0 1 2] and target = 4
Output : 0
NOTE : Think about the case when there are duplicates. Does your current solution work? How does the time complexity change?*
"""
class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def search(self, A, B):
        pivot = len(A)-1
        index = None
        first = 1
        last = len(A)-1
        while(first<=last):
            mid = (first+last)//2
            if mid-1 > 0 and  A[mid] < A[mid-1] and A[mid] < A[mid+1]:
                pivot = mid
                break
            elif  A[last] > A[mid]:
                last = mid - 1
            else:
                first = mid + 1
            
        index = self.BinarySearch(A, 0, pivot-1, B)
        if index == -1:
            index = self.BinarySearch(A, pivot, len(A)-1, B)
        return index
                
    def BinarySearch(self, A, first, last, X):
        mid = 0
        while(first<=last):
            mid = (first+last)>>1            
            if A[mid] == X:
                return mid         
            elif A[mid] > X:
                last = mid - 1
            elif A[mid] < X:
                first = mid + 1
        return -1 
