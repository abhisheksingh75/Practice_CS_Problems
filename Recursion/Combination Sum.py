"""
Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. The same repeated number may be chosen from C unlimited number of times.
 Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The combinations themselves must be sorted in ascending order.
CombinationA > CombinationB iff (a1 > b1) OR (a1 = b1 AND a2 > b2) OR ... (a1 = b1 AND a2 = b2 AND ... ai = bi AND ai+1 > bi+1)
The solution set must not contain duplicate combinations.
Example, Given candidate set 2,3,6,7 and target 7, A solution set is:
[2, 2, 3]
[7]

"""
def backtrackingCombinationSum(A, result, temp_set,temp_sum, start, sum):
    
    if sum == temp_sum:
        result.append(temp_set[:])
    elif temp_sum >sum:
        return
    else:
        dic_unique = {}
        for i in range(start,len(A)):
            if A[i] not in dic_unique:
                dic_unique[A[i]] = 1
                temp_set.append(A[i])
                temp_sum += A[i]
                backtrackingCombinationSum(A,result,temp_set,temp_sum,i, sum)
                temp_set.pop()
                temp_sum -= A[i]
                
            

class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of list of integers
	def combinationSum(self, A, B):
	    A.sort()
	    result = []
	    backtrackingCombinationSum(A,result, [], 0,0, B)
	    return result

