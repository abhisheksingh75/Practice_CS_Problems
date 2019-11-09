"find all subsets"""
"""
#recusrive solution
def recursiveSubset(list, result, subsetList):
        

        if list == []:
            result.append(subsetList[:])
        else:
            ele = list[0]
            list = list[1:]
            recursiveSubset(list,result, subsetList)
            subsetList.append(ele)
            recursiveSubset(list,result, subsetList)
            subsetList.pop()
            
        return 
    

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        result = []
        recursiveSubset(sorted(A), result, [])
        #print(result)
        #result.pop()
        result = sorted(result)
        return result
        
"""    
#backtracking solution

def backtrackSubsets(list, result, sub_list, start, end):
    
    result.append(sub_list[:])
    
    for i in range(start, end):
        sub_list.append(list[i])
        backtrackSubsets(list, result, sub_list, i+1,end)
        sub_list.pop()
    return

class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        result = []
        backtrackSubsets(sorted(A), result, [], 0, len(A))
        return result
        
