"""
Given a list of unique words A, find all pairs of distinct indices (i,j) in the given list such that concatenation of the two words, i.e. A[i] + A[j] is a palindrome. Note: A string is a palindrome if it reads the same backward as forward.
Input Format
The only argument given is the integer array A.
Output Format
Return the list of all pairs of distinct indices such that concatenation of the two words, i.e. A[i] + A[j] is a palindrome. 
You can return the list in any order.
Constraints
1 <= length of the list A <= 1000
100 <= lenght of words in list A <= 100
For Example
Input 1:
    A = ["abcd", "dcba", "lls", "s", "sssll"]
Output 1:
    [ [0,1], [1,0], [3,2], [2,4] ] 

Input 2:
    A = ["abc", "sa", "xy", "as" ]
Output 2:
    [ [1,3], [3,1] ]
 """
 def isPalindrome(Array):
    N = len(Array)
    i = 0 
    if N ==0:
        return True
        
    while(i<N//2):
        if Array[i] == Array[N-1-i]:
            i += 1
            continue
        else:
            return False
        
        
    return True
    

class Solution:
    # @param A : list of strings
    # @return a list of list of integers
    def solve(self, A):
        dic_revA = {}
        ans = []
        #create dictionary in reverse order
        for i in range(len(A)):
            ele = A[i][::-1]
            if ele not in dic_revA:
                dic_revA[ele] = i

        #print(dic_revA)
        #loop for element in list
        for i in range(len(A)):
            ele = A[i]
            length = len(ele)
            #loop for length of ele
            for k in range(0,len(ele)+1,1):
                
                prefix_first = ele[0:k]
                prefix_second = ele[k:length]
                suffix_first = ele[length-k:length]
                suffix_second = ele[0:length-k]
                
                
                if (prefix_first in dic_revA and 
                dic_revA[prefix_first] != i and
                isPalindrome(prefix_second) == True):
                    
                    if [i,dic_revA[prefix_first]] not in ans:  
                        ans.append([i,dic_revA[prefix_first]])
                
                if (suffix_first in dic_revA and
                    dic_revA[suffix_first] != i and
                    isPalindrome(suffix_second) == True):
                    if [dic_revA[suffix_first], i] not in ans:
                        ans.append([dic_revA[suffix_first], i])
                    
        return ans
                    
