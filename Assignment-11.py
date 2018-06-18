
#Question-1
class Animal:
    def animal_attribute(self):
        print("1.It has 4 legs")
        print("2.It is carnivores")
        print('\n')

class Tiger(Animal):
    def __init__(self):
        print("The name of Animal is Tiger")

obj2=Tiger()
obj2.animal_attribute()

#Question-2
# A B
# A B

#Question-3
class Cop:


    def addDetails(self,nm,agg,dess,wpp):
        self.name=nm
        self.age=agg
        self.designation=dess
        self.workExp=wpp
        print("Added Name of officer is %s"%(self.name))
        print("Added Age of Officer is %d"%(self.age))
        print("Added designation of officer is %s"%(self.designation))
        print("Added Work Experience of Officer is %d"%(self.workExp))
        print('\n')

    def dispplay(self):
        print(" Name of officer is %s" % (self.name))
        print(" Age of Officer is %d" % (self.age))
        print(" Designation of officer is %s" % (self.designation))
        print(" Work Experience of Officer is %d" % (self.workExp))
        print("\n")

    def update(self,nmm,aggg,desss,wppp):
        self.name = nmm
        self.age = aggg
        self.designation = desss
        self.workExp = wppp
        print("Updated Name of officer is %s" % (self.name))
        print("Updated Age of Officer is %d" % (self.age))
        print("Updated designation of officer is %s" % (self.designation))
        print("Updated Work Experience of Officer is %d" % (self.workExp))
        print('\n')


class Mission(Cop):
    def add_mission_details(self,mission):
        self.MissionDetails=mission
        print("The Mission of %s is %s"%(self.name,self.MissionDetails))
        print('\n')


obj3=Mission()
obj3.addDetails("Pradeep Tyagi",37,"IPS",10)
obj3.dispplay()
obj3.add_mission_details("To Solve Nirbhaya Case")

obj4=Mission()
obj4.addDetails("Shivam Nair",32,"Sho",5)
print("Opps entered wrong details..")
print("Updating officer details..")
print('\n')
obj4.update("Shubham Sharma",35,"Commisioner",6)
obj4.dispplay()
obj4.add_mission_details("To solve 26/11 case")




#Question-4
class Shape:
    def __init__(self,length,breadth):
        self.l=length
        self.b=breadth

    def Area(self):
            print("Area  is %d"%(self.l*self.b))


class Rectangle(Shape):
    def __init__(self,ln,bd):
        self.lengthh=ln
        self.bdd=bd


    def Area(self):
        print("Area of rectangle is : %d"%(self.lengthh*self.bdd))

class Square(Shape):
    def __init__(self,s):
        self.side=s

    def Area(self):
        print("Area of Square is :%d"%(self.side*self.side))


obj=Rectangle(5,6)
obj1=Square(4)
obj.Area()
obj1.Area()
