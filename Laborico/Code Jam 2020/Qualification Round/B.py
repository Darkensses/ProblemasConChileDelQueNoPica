inp=input
iinp= lambda: int(inp())
o=ord
def resolver():
    s=inp()
    res=''
    profundidad=0
    for i in s:
        n=o(i)-48
        res+='('*(n-profundidad)
        res+=')'*(profundidad-n)
        res+=i
        profundidad=n
    res+=')'*profundidad
    return res
     
t=iinp()
for i in range(t):
    res=resolver()
    print("Case #%i: %s"%(i+1,res))