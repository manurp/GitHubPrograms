# Sum of digits of a number
def sod(n):
	sum=0
	n1=n
	while n1!=0:
		d=n1%10
		sum+=d
		n1=int(n1/10)
	return(sum)

a=int(input("->"))
b=sod(a)
print("Sum of digits of %d = %d" %(a,b))