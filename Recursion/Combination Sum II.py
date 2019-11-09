"""
Combination Sum II
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. Each number in C may only be used once in the combination.
 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
Example : Given candidate set 10,1,2,7,6,1,5 and target 8, A solution set is:
[1, 7]
[1, 2, 5]
[2, 6]
[1, 1, 6]
"""
def backtrackingCombinationSum(A, result, temp_set, start, sum):
    
    if sum == 0:
        result.append(temp_set[:])
    elif sum < 0:
        return
    else:
        dic_unique = {}
        for i in range(start,len(A)):
            if A[i] not in dic_unique:
                dic_unique[A[i]] = 1
                temp_set.append(A[i])
                backtrackingCombinationSum(A,result,temp_set,i+1, sum-A[i])
                temp_set.pop()
                
            

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of list of integers
	def combinationSum(self, A, B):
	    A.sort()
	    result = []
	    backtrackingCombinationSum(A,result, [],0, B)
	    return result
