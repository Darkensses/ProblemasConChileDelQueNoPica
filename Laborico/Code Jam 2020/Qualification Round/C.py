inp=input
iinp= lambda: int(inp())
li=lambda: list(map(int,inp().split(" ")))
ls=lambda x: len(set(x))


def resolver():
    res=''
    ban=True
    n=iinp()
    C=[]
    J=[]
    s=[]
    for i in range(n):
        s.append(li())
    ss=sorted(s)
    for i in range(n):
        if len(C)==0:
            C.append(ss[i])
        else:
            bc=False
            for j in range(len(C)):
                if ss[i]==C[j]:
                    bc=True
                    break 
                elif ss[i][0]>=C[j][1]: pass
                elif ss[i][1]<=C[j][0]: pass
                else:
                    bc=True
                    break
            if not bc:
                C.append(ss[i])
            else:
                if len(J)==0:
                    J.append(ss[i])
                else:
                    bj=False
                    for j in range(len(J)):
                        if ss[i]==J[j]:
                            bj=True
                            break
                        elif ss[i][0]>=J[j][1]: pass
                        elif ss[i][1]<=J[j][0]: pass
                        elif ss[i][0]<J[j][0] and ss[i][0]<=J[j][0]:pass 
                        else:
                            bj=True
                            break
                    if not bj:
                        J.append(ss[i])
                    else:
                        ban=False
    if ban:
        for i in range(n):
            lon=len(C)
            for j in range(lon):
                if s[i]==C[j]:
                    res+='C'
                    C.pop(j)
                    lon-=1
                    break
            else:
                res+='J'
        return res
    else:
        return "IMPOSSIBLE"


t=int(input())
for i in range(t):
    res=resolver()
    print("Case #%i: %s"%(i+1,res))