

def GCprecentage(s):
    cG = s.count('G')
    cC = s.count('C')
    return 100 * (cG + cC) / len(s)


def getSeq(fd):
    while True:
        name = fd.readline().strip()
        seq = fd.readline().strip()
        if not name:
            return
        yield name, seq


if __name__ == '__main__':
    fd = open('rosalind_gc.txt', 'r')
    maxN = ''
    maxC = 0
    for name, seq in getSeq(fd):
        curC = GCprecentage(seq)
        print(curC)
        if curC > maxC:
            maxC = curC
            maxN = name
    print(maxN)
    print(maxC)
