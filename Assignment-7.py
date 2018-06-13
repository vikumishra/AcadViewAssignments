
#Question-1
rad=float(input("Enter radius"))
def area(r):
    return(3.14*r*r)

ar=area(rad)
print("Area of circle is %f"%(ar))
print('\n')



#Question-2
li=[]
def perfect(n):
    sum = 0
    for i in range(1,n):
        if(n%i==0):
            sum=sum+i
    if(n==sum):
        return n
for i in range(1,1000):
    k=perfect(i)
    if(isinstance(k,int)):
        li.append(k)
print('Perfect numbers between 1 and 1000 are')
print(li)
print('\n')



#Question-3

def table(n,k):
    if(k<=10):
        print("%d * %d = %d"%(n,k,n*k))
        table(n,k+1)

table(12,1)
print('\n')


#Question-4
a=int(input("Enter the base..."))
b=int(input("Enter the power..."))

def power(a,b):
    k=1
    if(b>0):
        k=a*power(a,b-1)
    return k

t=power(a,b)
print("%d raise to power %d is %d"%(a,b,t))
print('\n')


#Question-5
p=int(input("Enter no. whose factorial is to be found"))
dic={}
def factorial(p):
    if(p==1):
        return 1
    else:
        t=p*factorial(p-1)
        return t
fact=factorial(p)
dic={p:fact}
print(dic)




