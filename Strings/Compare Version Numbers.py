"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character. The . character does not represent a decimal point and is used to separate number sequences. For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision. Here is an example of version numbers ordering:
0.1 < 1.1 < 1.2 < 1.13 < 1.13.4
"""
def calcVersion(A):
    
    list_v = list(map(int, A.split(".")))
    while len(list_v) > 0:
        if list_v[-1] == 0:
           list_v.pop() 
        else:
            break
    return list_v

class Solution:
	# @param A : string
	# @param B : string
	# @return an integer
    def compareVersion(self, A, B):
        v1 = calcVersion(A)
        v2 = calcVersion(B)

        for i in range(min(len(v1),len(v2))):
            
            if v1[i] > v2[i]:
                return 1
            elif v1[i] == v2[i]:
                continue
            else:
                return -1
                
        if len(v1) > len(v2):
            return 1
        elif len(v1) < len(v2):
            return -1
        else:
            return 0
        
        
                
