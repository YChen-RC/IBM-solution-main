n = int(input())
valid = True
res = []
for _ in range(n):
    line = input().split()
    if line[1] == 'false':
        valid = False
        res.append(line[2])
if not valid:
    print("No")
    for i in range(len(res)):
        if i:
            print(" ", end="")
        print(res[i], end="")
else:
    print("Yes")

# 5
# 1 false ERR_00M
# 2 true
# 3 false ERR_TIME_OUT
# 4 true
# 5 true
