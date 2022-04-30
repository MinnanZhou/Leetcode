class Solution:
    def validTicTacToe(self, board) -> bool:
        check = ''
        for row in board: check += row
        xc, oc = check.count('X'), check.count('O')

        def win(player):
            if any(r == player * 3 for r in board): return True
            cols = ['', '', '']
            for r in board:
                cols[0] += r[0]
                cols[1] += r[1]
                cols[2] += r[2]
            if any(c == player * 3 for c in cols): return True
            if board[0][0] == board[1][1] == board[2][2] == player: return True
            if board[0][2] == board[1][1] == board[2][0] == player: return True
            return False

        statusO, statusX = win('O'), win('X')
        if not statusO and not statusX and (xc == oc + 1 or xc == oc): return True
        if statusO and not statusX and xc == oc: return True
        if statusX and not statusO and xc == oc + 1: return True
        if statusX and statusO: return False
        return False


a = Solution()
inp = ["XXX","XOO","OO "]
print(a.validTicTacToe(inp))
