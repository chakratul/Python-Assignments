class student:

    def __name(self):
        return self.__name
        
    def __rollNumber(self):
        return self.__rollNumber

    def getName(self):
        return self.__name
    def setName(self,name):
        self.__name = name

    def getRollNumber(self):
        return self.__rollNumber
    def setRollNumber(self,rollnumber):
        self.__rollNumber = rollnumber


obj = student()
obj.setName("Amit Singh")
print(obj.getName())
obj.setRollNumber(2552)
print(obj.getRollNumber())