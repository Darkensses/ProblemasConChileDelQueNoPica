inp=input
li=list
iinp=lambda : int(inp())
ent=lambda : map(int,inp().split())
lient=lambda : [int(i) for i in inp().split()]
li0= lambda x: [0 for i in range(x)]
stent=lambda : [i for i in inp()]

def resolver():
    res=0
    n=iinp()
    picos=lient()
    for i in range(1,n-1):
        if picos[i]>picos[i-1] and picos[i]>picos[i+1]: res+=1
    return res

t=iinp()
for i in range(t):
    res=resolver()
    print('Case #%i: %s'%(i+1,res))