class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        tmp = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                tmp.append(matrix[i][j])
        print(tmp)
        left = 0
        right = len(tmp)-1

        while left <= right:
            mid = (right + left) // 2
            print(mid)

            if target == tmp[mid]:
                return True
            
            if target > tmp[mid]:
                left = mid + 1
            elif target < tmp[mid]:
                right = mid - 1
        
        return False
