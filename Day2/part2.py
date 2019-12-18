def init():
    f = open("input.txt", "r")
    content = f.read()
    content = content.split(",")
    for i in range(len(content)):
        content[i] = int(content[i])
    else:
        f.close()
        return content


def mem(array, noun, verb):
    temp = array.copy()
    temp[1] = noun
    temp[2] = verb
    idx = 0;
    op = temp[idx]
    while op != 99:
        in1 = temp[idx + 1]
        in2 = temp[idx + 2]
        store = temp[idx + 3]
        if op == 1:
            temp[store] = temp[in1] + temp[in2]
        elif op == 2:
            temp[store] = temp[in1] * temp[in2]
        else:
            print("Invalid op code {} at index {}".format(op, idx))
            print(temp)
            break;
        idx += 4
        op = temp[idx]
    else:
        return temp[0]


for n in range(100):
    for v in range(100):
        ls = init()
        if mem(ls, n, v) == 19690720:
            print(mem(ls,n,v))
            print("100 * noun + verb = {}".format(100*n + v))
            print("n = {} v = {}".format(n, v))