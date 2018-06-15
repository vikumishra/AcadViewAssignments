#Question-1
class Circle:
    def __init__(self,rad):
        self.r=rad

    def getArea(self):
        self.area=3.14*self.r*self.r
        print("area of circle is ")
        print(self.area)
    def getCircumfrence(self):
        self.circumfrence=2*3.14*self.r
        print("Circumfrence of circle is")
        print(self.circumfrence)
obj=Circle(7)
obj.getArea()
obj.getCircumfrence()

#Question-2
class Student:
    def __init__(self,nam,rolno):
        self.name=nam
        self.rollno=rolno
    def display(self):
        print("Name:"+self.name)
        print("Roll no: %d"%(self.rollno))
obj1=Student("Viku",11501102)
obj1.display()

#Question-3
class Temperature:
    def convertFarenheit(self,cel):
        self.farenheit=(cel*1.8)+32
        print("Equivalent fareinheit for %f celcius is %f"%(cel,self.farenheit))
    def convertCelcius(self,far):
        self.celcius=(far-32)*.5556
        print("Equivalent Celcius for %f farenheit is %f"%(far,self.celcius))

obj2=Temperature()
obj2.convertFarenheit(30)
obj2.convertCelcius(50)

#Question-4
class MovieDetail:
    def __init__(self,mnam,arnam,yr,rat):
        self.MovieName=mnam
        self.ArstistName=arnam
        self.YearOfRelease=yr
        self.Ratings=rat
    def display(self):
        print("Movie Name: "+self.MovieName)
        print("Artist Name: "+self.ArstistName)
        print("Year Of Release: "+str(self.YearOfRelease))
        print("Ratings :"+str(self.Ratings))
    def update(self,umnam,uarnam,uyr,urat):
        self.MovieName = umnam
        self.ArstistName = uarnam
        self.YearOfRelease = uyr
        self.Ratings = urat
        print(" Updated Movie Name: " + self.MovieName)
        print("Updated Artist Name: " + self.ArstistName)
        print("Updated Year Of Release: " + str(self.YearOfRelease))
        print("Updated Ratings :" + str(self.Ratings))
obj3=MovieDetail("Shewshank Redemption","Arbninan",1995,9.5)
obj3.display()
obj3.update("3-idiots","Amir Khan",2008,9.0)

#Question-5
class Expenditure:
    def __init__(self,exp,sav):
        self.expenditure=exp
        self.savings=sav
    def displayExpenditureAndSavings(self):
        print("Expenditure is : %d"%(self.expenditure))
        print("Savings is : %d"%(self.savings))
    def calculateSalary(self):
        self.tot=self.expenditure+self.savings
    def displaySalary(self):
        print("Salary is :%d"%(self.tot))
obj4=Expenditure(12000,35000)
obj4.displayExpenditureAndSavings()
obj4.calculateSalary()
obj4.displaySalary()
