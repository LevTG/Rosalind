
def LetterCount(s):
    print(s.count('A'), end=' ')
    print(s.count('C'), end=' ')
    print(s.count('G'), end=' ')
    print(s.count('T'))

if __name__ == '__main__':
    fd = open('rosalind_dna.txt', 'r')
    s = fd.readline().strip()
    LetterCount(s)