"""
Given a string s, partition s such that every string of the partition is a palindrome. Return all possible palindrome partitioning of s. For example, given s = "aab", Return
  [
    ["a","a","b"]
    ["aa","b"],
  ]
 Ordering the results in the answer : Entry i will come before Entry j if :
len(Entryi[0]) < len(Entryj[0]) OR
(len(Entryi[0]) == len(Entryj[0]) AND len(Entryi[1]) < len(Entryj[1])) OR * * *
(len(Entryi[0]) == len(Entryj[0]) AND ... len(Entryi[k] < len(Entryj[k]))
In the given example, ["a", "a", "b"] comes before ["aa", "b"] because len("a") < len("aa")
"""

def palindromeIsPossible(string):
    i = 0
    N = len(string)
    if N <= 1:
        return True
    while(i<N//2):
        #print("i :"+str(i)+"N :"+str(N))
        if string[i] != string[N-1-i]:
            return False
        i += 1
    return True


def backtrackingPartition(result, tmp_list, curr_row, N, A):
    
    if curr_row == N:
        result.append(tmp_list[:])
    else:
        tmp = ""
        for i in range(curr_row, N):
            tmp += A[i]
            if palindromeIsPossible(tmp) == True:
                tmp_list.append(tmp)
                backtrackingPartition(result, tmp_list, i+1, N, A)
                tmp_list.pop()



class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        result = []
        N = len(A)
        tmp_list = []
        backtrackingPartition(result,[], 0, len(A), A)
        return result
