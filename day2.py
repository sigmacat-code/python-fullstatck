###########conditional statements##########################
# for i in range(1,11):
 #   print("good morning students! ")


  #  i=1
 #   while i<=5:
  #      print("good morning students! ")
    #    i += 1    

######################FUNCTION####################################

# def greet():
#     print("hello students! ")
#     print("welcome to python programming! ")

# greet()


###########################################################

# def add(a,b):
#     result = a + b
#     print(result)
# add(10,20)
# add(50,60)
####################LISTS###################################

# student = ["john", "jane", "doe", "smith"]
# print(student[0:])
#########################################################


# student = ["john", "jane", "doe", "smith"]
# student.append("krishna")
# student.remove("smith")
# student.insert(1,"ram")
# print(student)

#############################TUPLE####################################

# student_details = ("john", 23,84.4,True)
# print(student_details[0])
##########################DICTIONARY####################################        



















##############################class and objetcs#####################################

# class Student: 
#     def display(self):
#         print("hello students! ")
#         print("welcome to python programming! ")

# s1 = Student()
# s1.display()
#####################################Contructor##########################################

# class Student:
#     def __init__(self,name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Marks:",self.marks)

# s1 = Student("john",23,84.4)
# s2 = Student("jane",22,90.5)
# s1.display()
# s2.display()
#####################Encapulation####################
# class student:
#     def __init__(self):
#         self.__marks = 0

#     def set_marks(self,marks):
#         self.__marks= marks

#     def show_marks(self):
#         print("student marks:",self.__marks)


# s1 = student()
# s1.set_marks(85.5)
# s1.show_marks()

#################INHERITANCE#########################

# class grandfather:
#     def land(self):
#         print("grandfather has a land")

# class father(grandfather) :
#     def house (self):
#         print("fatheer has a house ")
# class son(father):
#     def car(self):
#         print("son has a car")
# class grandson(son):
#     def scooty (self):
#         print("grandson has a scooty ")
# class dhanush(grandson):
#     def dhanushree(self):
#         print("grandson gave her duaghter to dhanush")
# class krishna(dhanush):
#     def gay(self):
#         print("krishana realise that he is a gay at the age of 20 ")

    

# s = krishna()
# s.land()
# s.house
# s.car()
# s.scooty()
# s.dhanushree()
# s.gay()

#####################CONDITION#################
# krishana = int(input ("krishana, Enter your age? "))
# if (krishana<18):
#     print("go and bend for augustin ");
# else:
#     print("cut you dig and give to augustin");

#########################polymorphsim###################

# class BOB:
#     def sound(self):
#         print("a bomb its falling from up")

# class BOMB(BOB):
#     def sound(self):
#         print("and it landed in land and it make damammmmmmmmm")

# class BLAST(BOMB):
#     def sound(self):
#         print("and it balst it rest in piece")

# BOB = [BOMB(),BLAST(),BOB()]

# for BOB in BOB:
    
#     BOB.sound()


###########################abstract class########################

# from abc import ABC, abstractmethod

# class payment(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass

# class UPI(payment):
#     def pay(self,amount):
#         print(f"paid{amount} using UPI")


# class Card(payment):
#     def pay(self,amount):
#         print(f"paid {amount}using Card")



# p1 = UPI()
# p2 = Card()
# p1.pay(1000)
# p2.pay(2000)