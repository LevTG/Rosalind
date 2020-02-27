
def NewRabbits(n, k):
    r = 1

    if n == 1:
        return r
    elif n == 2:
        return k

    oG = NewRabbits(n - 1, k)
    tG = NewRabbits(n - 2, k)

    if n <= 4:
        return oG + tG
    return oG + tG * k

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    print(NewRabbits(n, k))
