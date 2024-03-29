import re


def init():
    f = open("input.txt", "r")
    wires = [[pair for pair in line.split(",")] for line in f]
    f.close()
    return wires


def grid_print(grid):
    for r in grid:
        for c in r:
            print(c, end=" ")
        print()


def make_grid(size):
    wires = init()
    max_len = size + 2
    rows, cols = (max_len * 2, max_len * 2)
    grid = [["." for i in range(cols)] for j in range(rows)]
    grid[max_len][max_len] = 'O'

    for wire in wires:
        row, col = (max_len, max_len)
        for item in wire:
            let = re.search("[a-zA-Z]", item).group().capitalize()
            num = int(re.search("[0-9]+", item).group())
            #print("=========== {} {} @ {},{} ===========".format(let, num, row, col))
            if let == 'R':
                for i in range(num):
                    row, col = (row, col + 1)
                    #print("Row: {} Col: {}".format(row,col))
                    if grid[row][col] == ".":
                        grid[row][col] = "-"
                    else:
                        grid[row][col] = "X"
                else:
                    grid[row][col] = "+"

            if let == 'L':
                for i in range(num):
                    row, col = (row, col - 1)
                    if grid[row][col] == ".":
                        grid[row][col] = "-"
                    else:
                        grid[row][col] = "X"
                else:
                    grid[row][col] = "+"

            if let == 'U':
                for i in range(num):
                    row, col = (row + 1, col)
                    if grid[row][col] == ".":
                        grid[row][col] = "|"
                    else:
                        grid[row][col] = "X"
                else:
                    grid[row][col] = "+"

            if let == 'D':
                for i in range(num):
                    row, col = (row - 1, col)
                    if grid[row][col] == ".":
                        grid[row][col] = "|"
                    else:
                        grid[row][col] = "X"
                else:
                    grid[row][col] = "+"

    return grid


def grid_dist(size, grid):
    dist = []
    max_len = size + 2
    rows, cols = (max_len * 2, max_len * 2)
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "X":
                x = abs(col-max_len)
                y = abs(row-max_len)
                #pair = (row, col)
                dist.append(x+y)
    dist.sort()
    return dist


def part1(size):
    paths = make_grid(size)
    distances = grid_dist(size, paths)
    return distances[0]


print(part1(9000))
