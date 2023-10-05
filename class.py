class person:
    name="surya"
    age= 22
    gender= "male"
    def getdetails(self,name,age,gender):
        self.name= input("enter the name")
        self.age=  int(input("enter the age"))
        self.gender= input("enter thr gender")
    def persondetails(self):
        print("Person details :\n",self.name , self.age ,self.gender)

pObj = person()
pObj.name="kiran"
pObj.age=25
pObj.persondetails()


