fuel = 0
f = open("input.txt", "r")
for line in f:
    div = int(line) // 3
    sub2 = div - 2
    fuel += sub2

print(fuel)
f.close()
