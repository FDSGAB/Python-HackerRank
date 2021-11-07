if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    listb = list()
    listc = list()
    for i in range (x+1):
        for j in range (y+1):
            for k in range (z+1):
                if ((i+j+k) != n):
                    listc.append(i)
                    listc.append(j)
                    listc.append(k)
                    listb.append(listc)
                listc = list()
    print(listb)
