class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        print("Checking row")
        print("=========================")
        for i in range(9):
            tmp = []
            for j in range(9):
                if board[i][j] != ".":
                    tmp.append(int(board[i][j]))
            set_tmp = set(tmp)
            print(f"TMP: {tmp}")
            print(f"SET: {set_tmp}")
            if len(tmp) != len(set_tmp):
                return False

        print("Checking column")
        print("=========================")
        for i in range(9):
            col_tmp = []
            for j in range(9):
                if board[j][i] != ".":
                    col_tmp.append(int(board[j][i]))
            set_col_tmp = set(col_tmp)
            if len(col_tmp) != len(set_col_tmp):
                return False

        print("Checking mat")
        print("=========================")
        for m in range(9):
            mat = []
            for i in range(3):
                for j in range(3):
                    row = (m // 3) * 3 + i
                    col = (m % 3) * 3 + j
                    if board[row][col] != ".":
                        mat.append(int(board[row][col]))
            set_mat = set(mat)
            if len(mat) != len(set_mat):
                return False

        return True
            
                