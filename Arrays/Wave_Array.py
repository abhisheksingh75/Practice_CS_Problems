"""https://www.interviewbit.com/problems/wave-array/
Given an array of integers, sort the array into a wave like array and return it, 
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

Example

Given [1, 2, 3, 4]

One possible answer : [2, 1, 4, 3]
Another possible answer : [4, 1, 3, 2]
 NOTE : If there are multiple answers possible, return the one thats lexicographically smallest. 
 """
 class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        lenOfA = len(A)
        A.sort()
        for i in range(len(A)):
            if (i+1)%2 != 0 and (i+1) < lenOfA:
                A[i], A[i+1] = A[i+1], A[i]
        return A
