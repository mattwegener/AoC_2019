f = open("input.txt", "r")
content = f.read()
a = content.split(",")
a[1] = "12"
a[2] = "2"


idx = 0;
op = int(a[idx])
while op != 99:
    in1 = int(a[idx + 1])
    in2 = int(a[idx + 2])
    store = int(a[idx + 3])
    if op == 1:
        a[store] = int(a[in1]) + int(a[in2])
    elif op == 2:
        a[store] = int(a[in1])*int(a[in2])
    else:
        print("Invalid op code {} at index {}".format(op, idx))
        print(a)
        break;
    idx += 4
    op = int(a[idx])
else:
    print(a)

f.close()