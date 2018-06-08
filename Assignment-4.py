#TUPLE QSN
#Question1
tupl=[1,2,3,'abc','def']
print(tupl.__len__())

#Question2
tupl1=[1,2,3,4,5,6]
print(max(tupl1))
print(min(tupl1))

#Question3
tupl2=[1*2*3*4*5*6]
print(tupl2)

#SETS QUESTION
a=input("enter number for first set")
b=input("enter number for first set")
c=input("enter number for first set")
d=input("enter number for first set")
e=input("enter number for first set")
f=input("enter number for second set")
g=input("enter number for second set")
h=input("enter number for second")
s1={a,b,c,d,e}
s2={f,g,h}
print(s1)
print(s2)

#Question1
s3=s1-s2
print(s3)

#Question2
s4=s1<=s2
s5=s1>=s2
print(s4)
print(s5)

#Question3
s6=s1&s2
print(s6)

#DICTIONARIES QUESTIONS
#Question1
dic={}
li=[]
name=["Vivek","Kunal","Rishav","Yogesh","Ajay","Prince","Abhimanyu","Raghav","Sanjeev","Rahul"]
mrks=[98,76,89,24,55,90,100,54,19,23]
for key in range(len(name)):
    dic[name[key]]=mrks[key]
print("Our dictionary is")
print(dic)
print("\n")

#Question2 (Optional Question)
dic={}
li=[]
name=["Vivek","Kunal","Rishav","Yogesh","Ajay","Prince","Abhimanyu","Raghav","Sanjeev","Rahul"]
mrks=[98,76,89,24,55,90,100,54,19,23]
for key in range(len(name)):
    dic[name[key]]=mrks[key]
print("Our dictionary is")
print(dic)

print("\n")

li=dic.values()
k=list(li)
print("Unsorted list of values of dictionary is")
print(k)
k.sort()
print("\n")
print("The Sorted list of dictionary is")
print(k)

#Question3
li=["M","I","S","S","I","S","S","I","P","P","I"]
M_count=li.count("M")
I_count=li.count("I")
S_count=li.count("S")
P_count=li.count("P")
dic1={"M-Counts":M_count,"I-Counts":I_count,"S-Counts":S_count,"P-Counts":P_count}
print("\n")
print(dic1)

