class person:
    def __init__(self,name):
        self.name=name
        self.DOB=self.Dob()

    def display(self):
        print('Name is=',self.name)
    class Dob:
        def __init__(self):
            self.dd=7
            self.mm=6
            self.yy=1998
        def display(self):
            print("DOB is= {}/{}/{}".format(self.dd,self.mm,self.yy))
if __name__ == '__main__':
    x=input("Enter a name: ")
    p=person(x)
    p.display()
    x = p.DOB
    x.display()
