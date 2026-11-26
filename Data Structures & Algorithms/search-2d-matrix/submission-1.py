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

        def find_row(matrix) :
            m = len(matrix)
            n = len(matrix[0])
            l = 0
            r = m-1

            while l <= r :
                mid_row = (l+r)//2
                
                if matrix[mid_row][0] <= target <= matrix[mid_row][n-1]:
                    return mid_row
                elif matrix[mid_row][0] > target :
                    r = mid_row - 1
                else :
                    l = mid_row + 1
                
            return False
        
        row = find_row(matrix)
        if row is False:
            return False 
        else :
            row = find_row(matrix)
            return binsearch(matrix[row])









