import math
def resursionGetPermutation(result, inputString, K, tmp):
    
    if result[1] == True:
        return
    if K <= 1:
        r1 = ''.join(tmp)
        r2 = ''.join(inputString)
        result[0] = r1 + r2
        result[1] = True
        return
    
    n = len(inputString)
    for i in range(n):
        factN = math.factorial(n-1)
        if (factN<K):
            K = K-factN
        else:
            tmp.append(inputString[i])
            inputString = inputString[:i] + inputString[i+1:]
            resursionGetPermutation(result,inputString, K, tmp)
            break
            
    return
    

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, A, B):
        result = ["", False]*2
        input = [0]*A
        for i in range(0, A):
            input[i] = str(i+1) 
        resursionGetPermutation(result, input, B, [])
        return result[0]import math
def resursionGetPermutation(result, inputString, K, tmp):
    
    if result[1] == True:
        return
    if K <= 1:
        r1 = ''.join(tmp)
        r2 = ''.join(inputString)
        result[0] = r1 + r2
        result[1] = True
        return
    
    n = len(inputString)
    for i in range(n):
        factN = math.factorial(n-1)
        if (factN<K):
            K = K-factN
        else:
            tmp.append(inputString[i])
            inputString = inputString[:i] + inputString[i+1:]
            resursionGetPermutation(result,inputString, K, tmp)
            break
            
    return
    

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, A, B):
        result = ["", False]*2
        input = [0]*A
        for i in range(0, A):
            input[i] = str(i+1) 
        resursionGetPermutation(result, input, B, [])
        return result[0]import math
def resursionGetPermutation(result, inputString, K, tmp):
    
    if result[1] == True:
        return
    if K <= 1:
        r1 = ''.join(tmp)
        r2 = ''.join(inputString)
        result[0] = r1 + r2
        result[1] = True
        return
    
    n = len(inputString)
    for i in range(n):
        factN = math.factorial(n-1)
        if (factN<K):
            K = K-factN
        else:
            tmp.append(inputString[i])
            inputString = inputString[:i] + inputString[i+1:]
            resursionGetPermutation(result,inputString, K, tmp)
            break
            
    return
    

class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def getPermutation(self, A, B):
        result = ["", False]*2
        input = [0]*A
        for i in range(0, A):
            input[i] = str(i+1) 
        resursionGetPermutation(result, input, B, [])
        return result[0]
