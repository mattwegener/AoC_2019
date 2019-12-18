
def calc_fuel(x):
    if x <=0:
        return 0
    else:
        return x // 3 - 2

total_fuel = 0
f = open("input.txt", "r")
for line in f:
    fuel = calc_fuel(int(line))
    while fuel > 0:
        total_fuel += fuel
        fuel = calc_fuel(fuel)

print(total_fuel)
f.close()