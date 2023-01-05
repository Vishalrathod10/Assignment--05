# CHALLANGE - 03

class student:
    def setname(self,name):
        self.__name = name

    def getname(self):
        return self.__name

    def setrollnumber(self,rollnumber):
        self.__rno = rollnumber

    def getrollnumber(self):
        return self.__rno


student_obj = student()
student_obj.setname('vishal')
print(student_obj.getname())
student_obj.setrollnumber(23)
print(student_obj.getrollnumber())

