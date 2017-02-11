def intreverse(n):
    ans=0
    while n:
        i=n%10
        n=int(n/10)
        ans=ans*10+i
    return(ans)

def matched(s):
    x=0 
    for i in range(len(s)):       
        if s[i]=="(":
            x=x+1
        elif s[i]==")":
            x=x-1
        if x<0:
            return(False)
    if x==0:
        return(True)
    else:
        return(False)


def factors(n):
    flist=[]
    for i in range(1,n+1):
        if n%i == 0:
            flist=flist+[i]
    return(flist)
def isprime(n):
    return(factors(n)==[1,n])
def sumprimes(l):
    ans=0
    for i in l:
        if isprime(i):
            ans=ans+i
    return(ans)
