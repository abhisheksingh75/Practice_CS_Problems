"""
Rearrange Array
Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space. Example:
Input : [1, 0]
Return : [0, 1]
 Lets say N = size of the array. Then, following holds true :
All elements in the array are in the range [0, N-1]
N * N does not overflow for a signed integer
"""



class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        old_value, new_value = 0, 0
        N =  len(A)
        for i in range(N):
            old_value = A[i]%N
            new_value = A[A[i]%N]%N
            #print("old_values "+str(old_value)+" new_value "+str(new_value))
            A[i] = new_value*N + old_value
        #print(A)
        for i in range(N):
            A[i] = A[i]//N
            #print(A)
        return A    
