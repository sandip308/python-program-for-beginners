class student:
    def __init__(self,name,m,r):
        self.name=name
        self.marks=m
        self.roll=r
    def display(self):
        print("Hi",self.name)
        print("You got {} marks".format(self.marks))
        print("Roll no is=",self.roll)
    def grade(self):
        if (self.marks>=750):
            print("You got first division")
        elif(self.marks>=600):
            print("You got second division")
        elif(self.marks>=350):
            print("You got third division")
        else:
            print("Unfortunately... You are failed")
if __name__ == '__main__':
    try:
        n = int(input("How many students in your class "))
        i = 0
        while i < n:
            x=input("Enter students name :")
            mark=eval(input("Enter student marks "))
            roll=int(input("Enter roll no "))
            s1=student(x,mark,roll)
            s1.display()
            s1.grade()
            i+=1
    except:
        print("There are some problem arise ")
