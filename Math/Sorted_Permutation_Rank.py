"""https://www.interviewbit.com/problems/sorted-permutation-rank/
Given a string, find the rank of the string amongst its permutations sorted lexicographically. 
Assume that no characters are repeated.

Example :

Input : 'acb'
Output : 2

The order permutations with letters 'a', 'c', and 'b' : 
abc
acb
bac
bca
cab
cba
The answer might not fit in an integer, so return your answer % 1000003

"""
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        if len(A) ==  1:
            return 1
        char_of_word = list(A)
        list_of_sort_alpha = list(A)
        list_of_sort_alpha.sort()
        no_of_chr_before = 0
        for charc in char_of_word:
            no_of_chr_before += self.find_pos(list_of_sort_alpha, charc)*math.factorial((len(list_of_sort_alpha)-1))
            list_of_sort_alpha.remove(charc)
            
        return no_of_chr_before+1
 
    def find_pos(self, list, char):
        for i in  range(0, len(list)):
            if list[i] == char:
                return i
