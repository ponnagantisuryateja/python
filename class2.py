class myclass:
    empname="suryateja"
    empno=12345
    gender="male"
    attendence="true"
    salary=123455
    def __init__(self,empname="kiran",empno=345678,gender="male",attendence="false",salary=50000):
        self.empname=empname
        self.empno=empno
        self.gender=gender
        self.attendence=attendence
        self.salary=salary
   # def display(self):
      #  print("the details of employee are:")
      #  print("employee name:", self.empname)
       # print("employee number:", self.empno)
       # print("employee gender:",self.gender)
       # print("employee attendence:", self.attendence)
       # print("employee salary:", self.salary)


obj=myclass("sai",23456,"female","false",45577)
#print(obj.empname,obj.attendence)
