class Emp:
    def __init__(self,n,s,i):
        self.name=n
        self.salary=s
        self.id=i
    def display(self):
        print("ID=",self.id)
        print("The employee name is=",self.name)
        print("The net salary is=",self.salary)
class sal:
    @staticmethod
    def sal_inc(self):
        self.salary+=1000
        self.display()
if __name__ == '__main__':
    try:
        name=input("Enter employee name: ")
        id=int(input("Enter employee id: "))
        salary=eval(input("Enter salary: "))
        e=Emp(name,salary,id)
        sal.sal_inc(e)
    except:
        print("There are some problem arise ")
