def resolver():
    s=input()
    res=''
    cont=0
    for i in s:
        n=ord(i)-48
        while cont<n:
            res+='('
            cont+=1
        while cont>n:
            res+=')'
            cont-=1
        res+=i
    for i in range(cont):
        res+=')'
    return res
     
t=int(input())
for i in range(t):
    res=resolver()
    print("Case #%i: %s"%(i+1,res))
