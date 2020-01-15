Median of Array
There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays ( The median of the array formed by merging both the arrays ). The overall run time complexity should be O(log (m+n)). Sample Input
A : [1 4 5]
B : [2 3]
Sample Output
3
class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return a double
    def findMedianSortedArrays(self, A, B):
        
        #keep first array as the smaller one
        if len(A) > len(B):
           return self.findMedianSortedArrays(B,A)
        
        n = len(A)
        m = len(B)
        low = 0
        high = len(A)
        
        while(low <= high):
            partitionX = (low + high)//2
            partitionY = (n+m+1)//2-partitionX
            #print("partitionX"+str(partitionX)+"partitionY"+str(partitionY))
            
            #calculate maxleftX
            if partitionX == 0:
                maxLeftX = -1*(1<<31)
            else:
                maxLeftX = A[partitionX-1]
            
            #calculate minRightX
            if partitionX >= n:
                minRightX = 1<<31
            else:
                minRightX = A[partitionX]
                
            #calculate minleftY
            if partitionY == 0:
                maxLeftY = -1*(1<<31)
            else:
                maxLeftY = B[partitionY-1]


            #calculate minRightY
            if partitionY >= m:
                minRightY = 1<<31
            else:
                minRightY = B[partitionY]
                
                
            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if ((m+n)%2 == 0):
                    #print("maxLeftX "+str(maxLeftX)+"maxLeftY "+str(maxLeftY)+"minRightX "+str(minRightX)+"minRightY "+str(minRightY))
                    return float(max(maxLeftX,maxLeftY))/2 + float(min(minRightX,minRightY))/2
                else:
                    return float(max(maxLeftX,maxLeftY))
            elif maxLeftX > minRightY:
                high = partitionX-1
            else:
                low = partitionX+1
    
        return         
                
                
            
                
            
            
                        
