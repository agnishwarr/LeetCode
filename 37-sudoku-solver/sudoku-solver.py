class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(index):
            if index == len(empty):
                return True

            r, c = empty[index]
            b = (r // 3) * 3 + (c // 3)

            for digit in '123456789':
                if digit not in rows[r] and digit not in cols[c] and digit not in boxes[b]:
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    boxes[b].add(digit)

                    if backtrack(index + 1):
                        return True

                    board[r][c] = '.'
                    rows[r].remove(digit)
                    cols[c].remove(digit)
                    boxes[b].remove(digit)

            return False

        backtrack(0)
