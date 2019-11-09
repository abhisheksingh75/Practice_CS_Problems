"""Given a collection of numbers that might contain duplicates, return all possible unique permutations. Example : [1,1,2] have the following unique permutations:
[1,1,2]
[1,2,1]
[2,1,1]
 NOTE : No 2 entries in the permutation sequence should be the same. Warning : DO NOT USE LIBRARY FUNCTION FOR GENERATING PERMUTATIONS. Example : next_permutations in C++ / itertools.permutations in python. If you do, we will disqualify your submission retroactively and give you penalty points.
 """
 
def backtrackPermute(list, result, tmp_list, N):
    
    if len(tmp_list) == N:
       result.append(tmp_list[:])
    else:
        #hash to track if number is repeating again & again
        dic_count = {}
        for i in range(len(list)):
            if list[i] not in dic_count:
                dic_count[list[i]] = 1
                tmp_list.append(list[i])
                backtrackPermute((list[:i]+list[i+1:]),result,tmp_list,N)
                tmp_list.pop()
    return

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
	def permute(self, A):
	    result = []
	    backtrackPermute(A, result, [], len(A))
	    return result

