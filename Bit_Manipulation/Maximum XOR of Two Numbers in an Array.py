"""
Given an array of integers A, find and return the maximum result of A[i] XOR A[j], where i, j are the indexes of the array.
"""

def addWord(Ele, head):
    
    curr = head
    for i in range(31,-1,-1):
        bit = (Ele>>i)&1
        #add this bit to curr node if this children doesn't exist
        if bit in curr.children:
            curr = curr.children[bit]
        else:
            newNode = trieNode(bit)
            curr.children[bit] = newNode
            curr = newNode
    curr.isTerminal = True
    return

def findMaxXOR(Ele,head):
    curr = head
    result = ""
    
    for i in range(31,-1,-1):
        bit = (Ele>>i)&1
        #add this bit to curr node if this children doesn't exist
        if bit == 0:
            if 1 in curr.children:
                curr = curr.children[1]
                result += str(1)
            else:
                curr = curr.children[0]
                result +=str(0)
        else:
            #when bit is equal to 0
            if 0 in curr.children:
                curr = curr.children[0]
                result += str(1)
            else:
                curr = curr.children[1]
                result +=str(0)
    return int(result, 2)
        

class trieNode:
    
    def __init__(self, ch):
        self.char = ch
        self.isTerminal = False
        self.children = {}

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        head = trieNode(None)
        for i in range(len(A)):
            addWord(A[i], head)
        maxXOR = -1
        for i in range(len(A)):
            currXOR = findMaxXOR(A[i], head)
            maxXOR = max(maxXOR, currXOR)
            
        return maxXOR
