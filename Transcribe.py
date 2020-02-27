
def Transcribe(s):
    print(s.replace('T', 'U'))


if __name__ == '__main__':
    fd = open('rosalind_rna.txt', 'r')
    s = fd.readline().strip()
    # s = input()
    Transcribe(s)
