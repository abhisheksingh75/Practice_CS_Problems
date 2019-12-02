"""
Given an integer N. Return count of minimum numbers, sum of whose squares is equal to N. Example: N=6 Possible combinations are :
(12 + 12 + 12 + 12 + 12 + 12)
(12 + 12 + 22)
So, minimum count of numbers is 3 (i.e. 1,1,2). Note: 1 ≤ N ≤ 105
"""
class Solution:
	# @param A : integer
	# @return an integer
	def countMinSquares(self, A):
        
        if A <= 3:
            return A
        MNS = [1<<31]*(A+1)
        MNS[0] = 0
        MNS[1] = 1
        MNS[2] = 2
        
        for i in range(3, A+1):
            j = 1
            while(j*j<=i):
                tmp = j*j
                if tmp > i:
                    break
                else:
                    MNS[i] = min(MNS[i], 1+MNS[i-tmp])
                j += 1
        return MNS[A]
        
