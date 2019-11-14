"""
Given a string, find the length of the longest substring without repeating characters. Example: The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""
class Solution:
	# @param A : string
	# @return an integer
	def lengthOfLongestSubstring(self, A):
        
        length,start,max_len = 0,0, -1*(1<<31) 
        dic_alpha = {}
        for i in range(len(A)):
            if A[i] not in dic_alpha:
               dic_alpha[A[i]] = i
               #print(dic_alpha)
            else:
                while(start<dic_alpha[A[i]]):
                    del dic_alpha[A[start]]
                    start += 1
                start = dic_alpha[A[i]]+1
                dic_alpha[A[i]] = i
                #print(dic_alpha)
            #print("start"+str(start)+"i:"+str(i))
            #print((i)+1)
            length = (i-start)+1
            #print("length"+str(length))
            max_len = max(max_len,length)
            i += 1
            
        return max_len
