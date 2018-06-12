
#Question-1
i=1
while(i<=10):
    a=input("Enter number")
    print(a)
    i = i + 1;

print('\n')


'''
#Question-2
while True:
    print("infinite") 
'''

#Question-3
a=[]
sq=[]
for i in range(0,2):
    k=int(input("Enter number for list"))
    a.append(k)
    sq.append(k*k)
print("Original list is")
print(a)
print("list after squaring its elements is")
print(sq)
print('\n')



#Question-4
a=[1,'abc',21.89,2,3,4.67,7.99,'pqr','stu']
ints=[]
flts=[]
str=[]
for i in a:
    if(isinstance(i,int)):
        ints.append(i)
    elif(isinstance(i,float)):
        flts.append(i)
    else:
        str.append(i)

print("Original List is")
print(a)
print("List of only integers is")
print(ints)
print("List of only floats is")
print(flts)
print("List of only string is")
print(str)


#Question-5
odd=[]
even=[]
for i in range(1101):
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print('\n')
print('List of even numbers upto 1101 is')
print(even)
print('List of odd numbers upto 1101 is')
print(odd)
print('\n')


#Question-6
for i in range(1,5):
    for j in range(1,i+1):
        print("*",end="")
    print('\r')



#Question-7
dic={}
name=["Vivek","Kunal","Rishav","Yogesh","Ajay","Prince","Abhimanyu","Raghav","Sanjeev","Rahul"]
mrks=[98,76,89,24,55,90,100,54,19,23]
for key in range(len(name)):
    dic[name[key]]=mrks[key]
print('\n')
print("Our dictionary is")
print(dic)
print('\n')
print("Keys of given dictionary are")
for key in dic:
    print(key)
print('\n')



#Question-8
li=[]
for i in range(5):
    k=int(input("Enter numbers"))
    li.append(k)
print(li)

fi=int(input("Enter no. to be find and deleted from list"))
for j in li:
    if(j==fi):
        li.remove(fi)
        print("List after removal of %d is "%(fi))
print(li)


