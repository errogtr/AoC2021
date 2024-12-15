from itertools import batched


N = 5


# puts -1 in place of y inside a board if y is in board
def update(board, y):
    return [-1 if x == y else x for x in board]


# produces a list with row-wise and column-wise sums for every board. The board wins if -5 is present.
def check(board):
    sums = [0] * 2 * N
    for i in range(len(board)):
        sums[i // N] += board[i]
        sums[i % N + N] += board[i]
    return -N in sums


# sum of not drawn numbers in a board
def sum_board(board):
    return sum(x for x in board if x != -1)


# every board is represented as a 'list' of 25 numbers
with open("day04/data", "r") as f:
    numbers = [int(x) for x in f.readline().split(",")]
    boards = batched([int(x) for x in f.read().split()], N**2)


# every time a number is drawn from the 'numbers' list the boards are updated and if some matches the
# winning condition (see the function 'check') they are removed from the boards list.
# When this happens, the product of the drawn number and the sum of remaining numbers in the boards
# are added to the 'win' list. The process continues while there are still boards to check.
win = list()
while boards:
    k = numbers.pop(0)
    boards = [update(b, k) for b in boards]
    for i, b in enumerate(boards):
        if check(b):
            win.append(k * sum_board(boards.pop(i)))

# ==== PART 1 ====
print(win[0])

# ==== PART 2 ====
print(win[-1])
