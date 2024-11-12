macierz=[]
x=1
y=1
for i in range(7):
    lista=[]
    for j in range(7):
        if i==0 or i==6 or j==0 or j==6:
            lista.append(1)
        else:
            lista.append(0)
    macierz.append(lista)
macierz[1][2]=1
macierz[2][2]=1
macierz[2][4]=1
macierz[2][5]=1
macierz[4][2]=1
macierz[4][3]=1
macierz[4][4]=1
macierz[5][4]=1
macierz[5][5]=3
macierz[1][1]=2
for k in range(7):
    print(macierz[k])
def rysujlabirynt(macierz,puste,sciana,ludzik,skarb):
    for el in macierz:
        t=""
        for i in el:
            if i==1:
                t=t+sciana
            elif i==2:
                t=t+ludzik
            elif i==3:
                t=t+skarb
            elif i==0:
                t=t+puste
        print(t)
def aktuallab(macierz,a,x,y):
    if a=="w":
        if macierz[y-1][x]!=1:
            macierz[y-1][x]=2
            macierz[y][x]=0
            y=y-1
        elif macierz[y-1][x]==1:
            print("Wszedłeś w ścianę")
    elif a=="s":
        if macierz[y+1][x]!=1:
            macierz[y+1][x]=2
            macierz[y][x]=0
            y=y+1
        elif macierz[y+1][x]==1:
            print("Wszedłeś w ścianę")
    elif a=="a":
        if macierz[y][x-1]!=1:
            macierz[y][x-1]=2
            macierz[y][x]=0
            x=x-1
        elif macierz[y][x-1]==1:
            print("Wszedłeś w ścianę")
    elif a=="d":
        if macierz[y][x+1]!=1:
            macierz[y][x+1]=2
            macierz[y][x]=0
            x=x+1
        elif macierz[y][x+1]==1:
            print("Wszedłeś w ścianę")
    return x,y
    print(rysujlabirynt(macierz, " ", "#", "o", "x"))
def gra(macierz,n):
    m=0
    x=1
    y=1
    rysujlabirynt(macierz," ","#","o","x")
    while x!=5 or y!=5 and m<n:
        a = input("podaj kierunek: ")
        x,y=aktuallab(macierz,a,x,y)
        m=m+1
        rysujlabirynt(macierz," ","#","o","x")
        if m == n:
            break
        elif x == 5 and y == 5:
            break
    if m == n:
        print("Przegrałeś")
    else:
        print("Gratulacje! Wygrałeś")
print(gra(macierz,20))