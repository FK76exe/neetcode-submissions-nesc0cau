class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        transposed_board = [["." for i in range(9)] for i in range(9)]
        for i, row in enumerate(board):
            # check validity
            if not self.areListElementsUnique(row):
                return False
            # if valid, send to transposed_board
            for j, elem in enumerate(row):
                # row[i][j] is transposed to row[j][i]
                transposed_board[j][i] = elem
        print(transposed_board)
        # assess cols
        for row in transposed_board:
            if not self.areListElementsUnique(row):
                return False
        # assess 3x3 boards
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subboard = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                if not self.areListElementsUnique(subboard):
                    return False
        return True

    def areListElementsUnique(self, elems: List[str]) -> bool:
        # covers row and col
        # len() is O(1) -> Python precomputes it
        nums = [i for i in range(1, 10)]
        for elem in elems:
            if elem == ".":
                continue
            elif nums[int(elem)-1] != 0:
                nums[int(elem)-1] = 0
            else:
                return False
        return True