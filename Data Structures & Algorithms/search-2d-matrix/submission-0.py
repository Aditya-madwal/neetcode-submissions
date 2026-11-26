class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = (0,0)
        m = len(matrix)
        n = len(matrix[0])
        right = (m-1,n-1)

        def binsearch(row) :
            l = 0
            n = len(row)
            r = n-1

            while l <= r :
                mid = (l+r)//2
                
                if row[mid] == target :
                    return True
                elif row[mid] < target :
                    l = mid+1
                else :
                    r = mid-1
                
            return False
        
        for i in range(len(matrix)) :
            row = matrix[i]

            if binsearch(row) :
                return True
        
        return False