import pickle
class Person:
    def __init__(self,name = None,phoneNumber = None,email = None):
        self.name = name
        self.phoneNumber = phoneNumber
        self.email = email

    def outputInfo(self):
        return f"Name: {self.name}, Phone: {self.phoneNumber}, Email: {self.email}"
    
    def checkClass(self):
        return "Person" 

class Student(Person):
    def __init__(self,name = None,phoneNumber = None,email = None,studentNumber=None,averageMark=None):
        super().__init__(name,phoneNumber,email)
        self.studentNumber = studentNumber
        self.averageMark = averageMark

    def outputInfo(self):
        return f"Name: {self.name}, Phone: {self.phoneNumber}, Email: {self.email}, Student Number: {self.studentNumber}, Average Mark: {self.averageMark}"
    
    def checkClass(self):
        return "Student"

class Professor(Person):
    def __init__(self,name=None,phoneNumber=None,email=None,salary=None):
        super().__init__(name,phoneNumber,email)
        self.salary = salary
    
    def outputInfo(self):
        return f"Name: {self.name}, Phone: {self.phoneNumber}, Email: {self.email}, salary: {self.salary}"
    
    def checkClass(self):
        return "Professor"



def inputClassList(objectList):
    for i in range(0,10):
        print(i+1)
        inputName = input("Enter the name: ")
        inputPhoneNumber = input("Enter the phone number: ")
        inputEmail = input("Enter the email address: ")
        objectList[i].name = inputName
        objectList[i].phoneNumber = inputPhoneNumber
        objectList[i].email = inputEmail
        if objectList[i].checkClass() == "Person":
            continue
        elif objectList[i].checkClass() == "Student":
            print(f"thong tin student {i+1}")
            inputStudentNumber = input("Enter the student number: ")
            inputAverageMark = input("Enter the average mark: ")
            objectList[i].studentNumber = inputStudentNumber
            objectList[i].averageMark = inputAverageMark
        else:
            print(f"thong tin professor {i+1}")
            inputSalary = input("Enter the salary: ")
            objectList[i].salary = inputSalary
    return objectList
if __name__ == "__main__":
    personList = [Person() for i in range(0,10)]
    inputClassList(personList)
    studentList = [Student() for i in range(0,10)]
    inputClassList(studentList)
    professorList = [Professor() for i in range(0,10)]
    inputClassList(professorList)
    for i in range(0,10):
        print(f"Person {i+1}")
        print(personList[i].outputInfo())
    for i in range(0,10):
        print(f"Student {i+1}")
        print(studentList[i].outputInfo())
    for i in range(0,10):
        print(f"Professor {i+1}")
        print(professorList[i].outputInfo())
    personList.sort(key = lambda x: x.name, reverse = True)
    studentList.sort(key = lambda x: x.averageMark, reverse = True)
    professorList.sort(key = lambda x: x.salary, reverse = False) 
    file1 = open("Person.txt","wb")
    for i in range(0,10):
        pickle.dump(personList[i].outputInfo(), file1)
    file1.close()
    file2 = open("Student.txt","wb")
    for i in range(0,10):
        pickle.dump(studentList[i].outputInfo(), file2)
    file2.close()
    file3 = open("Professor.txt","wb")
    for i in range(0,10):
        pickle.dump(professorList[i].outputInfo(), file3)
    file3.close()
    for i in range(0,10):
        print(f"Person {i+1}")
        print(personList[i].outputInfo())
    for i in range(0,10):
        print(f"Student {i+1}")
        print(studentList[i].outputInfo())
    for i in range(0,10):
        print(f"Professor {i+1}")
        print(professorList[i].outputInfo())