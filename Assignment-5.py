#Question-1
y=input("Enter year")
if(int(y)%4==0 ):
    print("Leap year")
else:
    print("Not a Leap year")

#Question-2
len=input("Enetr length")
brd=input("Enter Breadth")
if(int(len)==int(brd)):
    print("Square")
else:
    print("Rectangle")
#Question-3
a=int( input (" enter age of first person"))
b=int(input ("enter age of second person"))
c=int(input("enter age of third person"))
if(a>b and a>c):
    print("first person is oldest")
elif(b>a and b>c):
    print("second person is oldest")
elif(c>a and c>b):
    print("third is oldest")
else:
    print("All are of same age")

if(a<b and a<c):
    print("first is youngest")
elif(b<a and b<c):
    print("second is youngest")
elif(c<a and c<b):
    print("third is youngest")


#Question-4
points=int(input("Enter points.. Not more then 200"))
if(points>=1 and points<=50):
    print("Sorry! No prize this time")
elif(points>=51 and points<=150):
    print("Congratulations! You won a Wooden Dog")
elif(points>=151 and points<=180):
    print("Congratulations! You won a Book")
elif(points>=181 and points<=200):
    print("Congratulations! You won Chocolates")
else:
    print("Please enter valid points")


#Question-5
q=int(input("Enter quantity"))
if(q*100>1000):
    print("Cost is "+str((q*100)-(0.1*q*100)))
else:
    print(q*100)

