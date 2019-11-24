"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining. 
Input Format
The only argument given is integer array A.
Output Format
Return the total water it is able to trap after raining..
For Example
Input 1:
    A = [0,1,0,2,1,0,1,3,2,1,2,1]
Output 1:
    6
Explaination 1:
#look for the solution with using additonal memory space?
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        
        stack = []
        i =0
        bounded_water = 0
        for i in range(len(A)):
            
            while(stack!=[] and A[i]>A[stack[-1]]):
                distance, height = 0,0
                ele_indx  = stack.pop()
                ele_height = A[ele_indx]
                if stack != []:
                    distance = i-stack[-1]-1
                    height = min(A[i],A[stack[-1]]) - ele_height
                bounded_water += (distance*height)
                     
                
            stack.append(i) 
            
        return bounded_water
