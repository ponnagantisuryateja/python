class person:

    def _getdetails(self):
        self.name= input("enter the name")
        self.age=  int(input("enter the age"))
        self.gender= input("enter thr gender")
        self.__persondetails()

    def __persondetails(self):
        print("Person details :\n",self.name , self.age ,self.gender)

pObj = person()
pObj._getdetails()


