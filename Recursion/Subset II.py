"""
Subsets II
Given a collection of integers that might contain duplicates, S, return all possible subsets.
 Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
The subsets must be sorted lexicographically.
Example : If S = [1,2,2], the solution is:
[
[],
[1],
[1,2],
[1,2,2],
[2],
[2, 2]
]
"""
def backtrackSubsets(list, result, sub_list, start, end):
    
    if sub_list not in result:
        result.append(sub_list[:])
    
    for i in range(start, end):
        sub_list.append(list[i])
        backtrackSubsets(list, result, sub_list, i+1,end)
        sub_list.pop()
    return

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        result = []
        backtrackSubsets(sorted(A), result, [], 0, len(A))
        return list(result)
        
