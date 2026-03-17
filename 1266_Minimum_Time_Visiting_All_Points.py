class Solution(object):
    def minTimeToVisitAllPoints(self, points):

        time = 0 
        for  i in range(len(points)-1):
            x_axis= abs(points[i][0]-points[i+1][0])
            y_axis=abs(points[i][1]-points[i+1][1])
            theoratical_moves = x_axis+y_axis
            non_diagonals=abs(y_axis-x_axis)
            diagonals=(theoratical_moves-non_diagonals)/2
            actual_moves=diagonals+non_diagonals
            time+=actual_moves
        return time


s  = Solution()
points = [[1,1],[3,4],[-1,0]]
print(s.minTimeToVisitAllPoints(points))