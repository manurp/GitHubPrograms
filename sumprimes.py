def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i==0:
                return(False)
        return(True)
    else:
        return(False)

def sumprimes(a):
    sum=0
    for i in range(0,len(a)):
        b=prime(a[i])
        if b:
            sum=sum+a[i]
    return(sum)
