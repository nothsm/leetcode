from typing import List, Set

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows and cols
        for i in range(len(board)):
            row: Set[str] = set()
            col: Set[str] = set()
            box: Set[str] = set()
            for j in range(len(board[i])):
                box_i: int = ((3*i) + (j // 3)) % 9
                box_j: int = (j % 3) + (3 * (i // 3))
                if board[i][j] in row and board[i][j] != ".":
                    return False
                if board[j][i] in col and board[j][i] != ".":
                    return False
                if board[box_i][box_j] in box and board[box_i][box_j] != ".":
                    return False
                row.add(board[i][j])
                col.add(board[j][i])
                box.add(board[box_i][box_j])
        return True