inp=input
iinp= lambda: int(inp())
li=lambda: list(map(int,inp().split(" ")))
ls=lambda x: len(set(x))
inv=lambda x: ''.join(str(1 - int(c)) for c in x)

def vol(res,res2,res3):
    res=inv(res)
    res2=inv(res2)
    res3=inv(res3)[::-1]
    tmpres=res
    res=res2[::-1]
    res2=tmpres[::-1]
    return res,res2,res3

def operaciones(tmp,tmp2,tmp3,res,res2,res3):
    tmpres,tmpres2,tmpres3=vol(res,res2,res3)
    if tmpres[0:2]==tmp and tmpres2[-2::]==tmp2 and tmpres3==tmp3:
        res,res2,res3=vol(res,res2,res3)
    elif tmp==inv(res[0:2]) and tmp3==inv(res3) and tmp2==inv(res2[0:2]):
        res=inv(res)
        res2=inv(res2)
        res3=inv(res3)
    elif tmp==res2[-2::] and tmp2==res[0:2] and tmp3==res3[::-1]:
        tmpres=res
        res=res2[::-1]
        res2=tmpres[::-1]
        res3=res3[::-1]
    return res,res2,res3

def cambios(res,res2,res3,n,m):
    tmp=tmp2=tmp3=''    
    print(1)
    tmp+=inp()
    print(2)
    tmp+=inp()
    print(19)
    tmp2+=inp()
    print(20)
    tmp2+=inp()
    print(n)
    tmp3+=inp()
    print(m)
    tmp3+=inp()
    return operaciones(tmp,tmp2,tmp3,res,res2,res3)

def llamadas(res,res2,res3,n,m,b):
    res,res2,res3=cambios(res,res2,res3,b//2,b//2+1)
    for i in range(n,n+2):
        print(i)
        res+=inp()
    for i in range(m,m-2,-1):
        print(i)
        res2=inp()+res2
    return res,res2,res3


def resolver(b):
    res=res2=res3=''
    if b==10:
        for i in range(1,11):
            print(i)
            res+=inp()
    if b==20:
        for i in range(1,5):
            print(i)
            res+=inp()
        for i in range(17,21):
            print(i)
            res2+=inp()
        for i in range(10,12):
            print(i)
            res3+=inp()

        n=5
        m=16
        for i in range(2):
            res,res2,res3=llamadas(res,res2,res3,n,m,b)
            n+=2
            m-=2


        res,res2,res3=cambios(res,res2,res3,b//2,b//2+1)

        for i in range(9,10):
            print(i)
            res+=inp()
        for i in range(12,11,-1):
            print(i)
            res2=inp()+res2
        res+=res3+res2
        
    if b==100:
        for i in range(1,5):
            print(i)
            res+=inp()
        for i in range(97,101):
            print(i)
            res2+=inp()
        for i in range(50,52):
            print(i)
            res3+=inp()
        
        n=5
        m=96
        for i in range(15):
            res,res2,res3=llamadas(res,res3,res3,n,m,b)
            n+=3
            m-=3
        
        res+=res3+res2

    print(res)
    a=inp()
    if a=='Y':
        return 1
    else:
        return 0

t,b=li()
for i in range(t):
    res=resolver(b)
    if res==0:
        break