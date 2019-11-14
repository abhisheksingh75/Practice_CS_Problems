"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence. Example: Given [100, 4, 200, 1, 3, 2], The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4. Your algorithm should run in O(n) complexity.
"""
class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
        max_length = 0
        dic_len = {}
        for i in range(len(A)):
            #if element exist just continue otherwise update the value in dic_len
            if A[i] not in dic_len:
                #check left length
                if A[i]-1 in dic_len:
                    left_len = dic_len[A[i]-1]
                else:
                    left_len = 0
                #check right length
                if A[i]+1 in dic_len:
                    right_len = dic_len[A[i]+1]
                else:
                    right_len = 0
                #update A[i] length
                dic_len[A[i]] = 1+left_len+right_len
                #update left ele length
                if left_len != 0:
                    dic_len[A[i]-left_len] = dic_len[A[i]]
                #update right ele length
                if right_len != 0:
                    dic_len[A[i]+right_len] = dic_len[A[i]]
                #update max_length value
                max_length = max(max_length,dic_len[A[i]])
        return max_length
