"""print all permutations"""

def printAllPermuation(A, res, tmpString):
    
    if len(A) == 1:
        res.append(tmpString)
    else:
        for i in range(len(A)):
            printAllPermuation(A[:i]+A[i+1:], res, tmpString+A[i])
            
            


class Sol:
    
    def solve(self, word):
        
        res = []
        printAllPermuation(word,res,"")
        return res

o_object = Sol()
print(o_object.solve("ABCD"))
