def egcd(a, b):
    if a % b == 0:
        # print("{} = {}(0) + {}(1)".format(b, a, b))
        print("{} = {}({}) + {}".format(a, b, a // b, a % b))
        return b, 0, 1
    else:
        tmp = egcd(b, a % b)
        # print(tmp[0], tmp[2], tmp[1] - (a // b)*tmp[2])
        # print("{} = {}({}) + {}({})".format(tmp[0], tmp[2], b, tmp[1] - (a // b) * tmp[2], a % b))
        print("{} = {}({}) + {}".format(a, b, a // b, a % b))
        return tmp[0], tmp[2], tmp[1] - (a // b)*tmp[2]

while True:
    a = int(input(">> a = "))
    b = int(input(">> b = "))
    print("EGCD({}, {}) = ".format(a, b))
    ans = egcd(a, b)
    print("{} = {}({}) + {}({})".format(ans[0], ans[2], a, ans[1] - (a // b) * ans[2], b))