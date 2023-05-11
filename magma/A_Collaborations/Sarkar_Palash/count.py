with open("./NOMA-codebook_n=6_exhaust.txt", 'w') as fp1:
    maxcnt = 0
    with open(r"./NOMA-codebook_n=6.txt", 'r') as fp:
        k = 0
        for line in fp:
            if "-" in line:
                k = 0
                fp1.write(line)
            if "[" in line:
                k = k + 1
                fp1.write(line)
            if ("-" not in line) and ("[" not in line):
                fp1.write("size={}\n".format(k))
                maxcnt = max(maxcnt, k)

print(maxcnt)
