
dic = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

def Complemente(s):
    s = s.translate(str.maketrans(dic))
    print(s[::-1])


if __name__ == '__main__':
    fd = open('rosalind_revc.txt', 'r')
    s = fd.readline().strip()
    # s = input()
    Complemente(s)
