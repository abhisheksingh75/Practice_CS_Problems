"""
You are given an array (zero indexed) of N non-negative integers, A0, A1 ,..., AN-1. Find the minimum sub array Al, Al+1 ,..., Ar so if we sort(in ascending order) that sub array, then the whole array should get sorted. If A is already sorted, output -1. Example :
Input 1:

A = [1, 3, 2, 4, 5]

Return: [1, 2]

Input 2:

A = [1, 2, 3, 4, 5]

Return: [-1]
In the above example(Input 1), if we sort the subarray A1, A2, then whole array A should get sorted.
"""
class Solution:
	# @param A : list of integers
	# @return a list of integers
	def subUnsort(self, A):
	    A =list(A)
        leftIndx, rightIndx = None, None
        local_min, local_max = 1<<31, -1*(1<<31)
        
        for i in range(len(A)-1):
            if A[i] <= A[i+1]:
                continue
            else:
                leftIndx = i
                break
                
        if leftIndx is None:
            return [-1]
        
        for i in range(len(A)-1, 0, -1):
            if A[i] >= A[i-1]:
                continue
            else:
                rightIndx = i 
                break
        
        for i in range(leftIndx, rightIndx+1, 1):
            local_min = min(local_min, A[i])
            local_max = max(local_max, A[i]) 
        

        for i in range(leftIndx):
            if A[i] > local_min:
                leftIndx = i
                break
            
        for i in range(len(A)-1,rightIndx, -1):
            #print("A[I]"+str(A[i])+"local_max"+str(local_max)+"i"+str(i))
            if A[i] < local_max:
                #print("alha")
                rightIndx = i
                break

        return [leftIndx, rightIndx]
            
            
            
