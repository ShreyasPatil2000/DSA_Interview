from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, columns, squares = defaultdict(set), defaultdict(set), defaultdict(set)
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                if board[row][col] in rows[row] or board[row][col] in columns[col] or board[row][col] in squares[(row//3, col//3)]:
                    return False
                rows[row].add(board[row][col])
                columns[col].add(board[row][col])
                squares[(row//3, col//3)].add(board[row][col])
        return True
        
    
ob = Solution()
print(ob.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))

# We initialize 3 defaultdict(set) as rows, columns and squares. There are 1-9 rows, 1-9 columns and (1-3,1-3) squares in the sudoku puzzle. While iterating through the puzzle, we check whether the board cell number is present in the dicts. If there is a ., we ignore it. If it's not there, we add it to the dicts but if its not we return False. At the end, we return True. 

# Time Complexity: O(1) its a 9x9 iteration 
# Space Complexity: O(1) its a 9x9 storage and we use 3 different dicts 