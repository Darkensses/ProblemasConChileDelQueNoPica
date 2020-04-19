inp=input
li=list
iinp=lambda : int(inp())
ent=lambda : map(int,inp().split())
lient=lambda : [int(i) for i in inp().split()]
li0= lambda x: [0 for i in range(x)]
stent=lambda : [i for i in inp()]

def revisar(medio,dias,n,d):
    s=dias[0]*medio
    for i in range(1,n):
        s=((s+dias[i]-1)//dias[i])*dias[i]
        if s>d: return 0
    return 1

def resolver():
    n,d=ent()
    dias=lient()
    ultimo=1
    divbus=d//dias[0]
    while ultimo<divbus:
        medio=(ultimo+divbus+1)//2
        if revisar(medio,dias,n,d):
            ultimo=medio
        else:
            divbus=medio-1
    return ultimo*dias[0]

t=iinp()
for i in range(t):
    res=resolver()
    print('Case #%i: %s'%(i+1,res))