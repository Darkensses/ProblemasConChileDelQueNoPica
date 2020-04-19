inp=input
li=list
iinp=lambda : int(inp())
ent=lambda : map(int,inp().split())
lient=lambda : [int(i) for i in inp().split()]
li0= lambda x: [0 for i in range(x)]
stent=lambda : [i for i in inp()]

from collections import Counter
limite=10**9

def leerordenes(ordenes,x,y):
    pos=Counter(ordenes)
    if 'W' in pos: x-=pos['W']
    if 'E' in pos: x+=pos['E']

    if 'N' in pos: y-=pos['N']
    if 'S' in pos: y+=pos['S']

    if x<=0: x+=limite
    if x>limite: x-=limite

    if y<=0: y+=limite
    if y>limite: y-=limite
    return x,y

def resolver():
    orde=inp()
    x=y=1
    if '(' not in orde:
        x,y=leerordenes(orde,x,y)
        return str(x)+" "+str(y)
    else:
        profundidad=[]
        for i in range(len(orde)):
            if orde[i].isdigit():
                profundidad.append(i)

        while len(profundidad):
            tmp=''
            indice=0
            for i in range(profundidad[-1]+2,len(orde)):
                if orde[i]==')':
                    break
                tmp+=orde[i]
                indice=i
            orde=orde[:profundidad[-1]]+(int(orde[profundidad[-1]]) * tmp)+orde[indice+2:]
            profundidad.pop(-1)
        x,y=leerordenes(orde,x,y)
        return str(x)+" "+str(y)

t=iinp()
for i in range(t):
    res=resolver()
    print('Case #%i: %s'%(i+1,res))