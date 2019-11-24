"""
Given an array of integers A of size N. A represents a histogram i.e A[i] denotes height of the ith histogram's bar. Width of each bar is 1. Largest Rectangle in Histogram: Example 1 Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3]. Largest Rectangle in Histogram: Example 2 The largest rectangle is shown in the shaded area, which has area = 10 unit. Find the area of largest rectangle in the histogram. 
Input Format
The only argument given is the integer array A.
Output Format
Return the area of largest rectangle in the histogram.
For Example
Input 1:
    A = [2, 1, 5, 6, 2, 3]
Output 1:
    10
    Explanation 1:
        The largest rectangle is shown in the shaded area, which has area = 10 unit.
       """
       def calcArea(hist,stack, i):
    area = 0
    ele_indx = stack.pop()
    ele_height = hist[ele_indx]
    if stack == []:
        area = ele_height*i
    else:
        area = ele_height*(i-stack[-1]-1)
    return area

class Solution:
	# @param A : list of integers
	# @return an integer
	def largestRectangleArea(self, A):
	    
        hist = A
        stack = []
        i = 0
	    max_area = -1
        while(i<len(hist)):
	        
            #push ele if stack is empty or top element is less than or equal to curr_ele
            if stack == [] or hist[stack[-1]]<=hist[i]:
                stack.append(i)
                i += 1
            else:
                area = calcArea(hist,stack, i)
                max_area  = max(max_area, area)
        
        #histogram traversed but elements are there in stacj        
        while(stack != []):
            
            area = calcArea(hist,stack, i)
            #print(area)
            max_area  = max(max_area, area)
        return max_area
            
	        
	        
	    
	    
