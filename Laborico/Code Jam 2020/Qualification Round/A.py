inp=input
iinp= lambda: int(inp())
li=lambda: list(map(int,inp().split(" ")))
ls=lambda x: len(set(x))

def resolver():
    res=''
    n=iinp()
    mat=[]
    b=[]
    k=r=c=0
    for i in range(n):
        a=li()
        mat.append(a)
        if ls(a)!=n:
            r+=1
    for i in range(n):
        k+=mat[i][i]
        for j in range(n):
            b.append(mat[j][i])
        if ls(b)!=n:
            c+=1
        b=[]
    res+=str(k)+" "+str(r)+" "+str(c)
    return res


t=iinp()
for i in range(t):
    res=resolver()
    print("Case #%i: %s"%(i+1,res))