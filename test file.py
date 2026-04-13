L = []
O = []
a = int(input())
def z():
    for i in range(a):
        L.append(int(input()))
    print(L)
    for i in L:
        if i % 2 == 0:
            O.append(i)
    print(O)
z()


    
    
    