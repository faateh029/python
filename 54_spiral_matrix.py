class Solution(object):
    def spiralOrder(self, matrix):
        m = len(matrix)
        n= len(matrix[0])
        arr=[]
        top = 0 
        bottom = m-1
        right = n-1
        left = 0
        while top<=bottom and left<=right:
            for i in range(left , right+1):
                arr.append(matrix[top][i])
            top=top+1
            if top>bottom or left>right:
                return arr
            for i in range(top ,bottom+1):
                arr.append(matrix[i][right])
            right=right - 1
            if top>bottom or left>right:
                return arr
            for i in range(right, left-1, -1):
                arr.append(matrix[bottom][i])
            bottom=bottom-1
            if top>bottom or left>right:
                return arr
            for i in range (bottom , top -1 , -1):
                arr.append(matrix[i][left])
            left=left+1 
        return arr
    
obj = Solution()

print(obj.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))