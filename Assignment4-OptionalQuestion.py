dic={}
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