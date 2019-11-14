"""
Find the largest continuous sequence in a array which sums to zero. Example:
Input:  {1 ,2 ,-2 ,4 ,-4}
Output: {2 ,-2 ,4 ,-4}
"""
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        
        dic_prefixSum = {}
        dic_prefixSum[0] = -1
        sum = 0
        ans = []
        tmp_ans = []
        for i in range(len(A)):
            sum += A[i]
            if sum in dic_prefixSum:
                tmp_ans = A[dic_prefixSum[sum]+1:i+1]
                if len(tmp_ans) > len(ans):
                    ans = tmp_ans
            else:
                dic_prefixSum[sum] = i
        return ans
