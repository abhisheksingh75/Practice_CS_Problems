"""
Given an array A of integers, find the index of values that satisfy A + B = C + D, where A,B,C & D are integers values in the array Note:
1) Return the indices `A1 B1 C1 D1`, so that 
  A[A1] + A[B1] = A[C1] + A[D1]
  A1 < B1, C1 < D1
  A1 < C1, B1 != D1, B1 != C1 

2) If there are more than one solutions, 
   then return the tuple of values which are lexicographical smallest. 

Assume we have two solutions
S1 : A1 B1 C1 D1 ( these are values of indices int the array )  
S2 : A2 B2 C2 D2

S1 is lexicographically smaller than S2 iff
  A1 < A2 OR
  A1 = A2 AND B1 < B2 OR
  A1 = A2 AND B1 = B2 AND C1 < C2 OR 
  A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
Example:
Input: [3, 4, 7, 1, 2, 9, 8]
Output: [0, 2, 3, 5] (O index)
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, Arr):
        ans = [0]*4
        dic_sum ={}
        A,B,C,D = 1<<31,1<<31,1<<31,1<<31
        tmp_A,tmp_B,tmp_C,tmp_D = 1<<31,1<<31,1<<31,1<<31
        for i in range(len(Arr)):
            for j in range(i+1, len(Arr)):
                if Arr[i]+Arr[j] in dic_sum:
                    # A< C AND B != C AND B!= D
                    if dic_sum[Arr[i]+Arr[j]][0] < i and dic_sum[Arr[i]+Arr[j]][1] != i and dic_sum[Arr[i]+Arr[j]][1] != j:
                        tmp_A = dic_sum[Arr[i]+Arr[j]][0]
                        tmp_B = dic_sum[Arr[i]+Arr[j]][1]
                        tmp_C = i
                        tmp_D = j 
                else:
                    dic_sum[Arr[i]+Arr[j]]= [i,j]
                    
                if tmp_A< A:
                    A,B,C,D = tmp_A,tmp_B,tmp_C,tmp_D
                elif tmp_A == A and tmp_B < B:
                     A,B,C,D = tmp_A,tmp_B,tmp_C,tmp_D
                elif tmp_A == A and tmp_B == B and tmp_C < C:
                    A,B,C,D = tmp_A,tmp_B,tmp_C,tmp_D
                elif tmp_A == A and tmp_B == B and tmp_C == C and tmp_D < D:
                    A,B,C,D = tmp_A,tmp_B,tmp_C,tmp_D
                    
        return [A,B,C,D]
