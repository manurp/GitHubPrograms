def descending(l):
    x=len(l)
    for i in range(1,x):
        if l[i]>l[i-1]:
            return(False)
    return(True)
#find if the list is in descending order using built in functions
def descend(l):
    l1=l[:]
    l1.sort()
    l1.reverse()
    if l1==l:
        return(True)
    return(False)
        
def alternating(l):
    l1=l[::2]
    l2=l[1::2]
    if len(l)<2:
        return(True)   
    if l1[0]>l2[0]:
        (l1,l2)=(l2,l1)
    x=len(l1)
    y=len(l2)
    for i in range(1,x):
        if l2[i]<=l1[i] or l2[i]<=l1[i-1]:
            return(False)
    if l2[y-1]<=l1[x-1]:
        return(False)
    return(True)

def matmult(m1,m2):
    res=[]
    for i in range(len(m1)):
        x=0
        m=[]
        while x<len(m1):
            ans=0
            for j in range(len(m1[0])):
                ans+=m1[i][j]*m2[j][x]
            m.append(ans)
            x+=1
        res.append(m)
    return(res)
