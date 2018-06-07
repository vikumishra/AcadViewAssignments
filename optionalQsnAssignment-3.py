li=[1,3,2,4,5,7,6,9,8,10,11]
odd=0
even=0

for x in li:
    if x%2==0:
     even=even+1
    else:
     odd=odd+1

print("Count of odd numbers in a list is %d"%(odd))
print("Count of even numbers in a list is %d"%(even))
