class Dog:
    def bark(self):
        print("Bow,wow ...")
class cat:
    def talk(self):
        print("Meow, meow")
class Human:
    def talk(self):
        print("Hi, Hello how are u")
def power_talk(obj):
    if hasattr(obj,'bark'):
        obj.bark()
    elif hasattr(obj,'talk'):
        obj.talk()
    else:
        print("Wrong object passed ")
if __name__ == '__main__':
    D=Dog()
    power_talk(D)
    C=cat()
    power_talk(C)
    H=Human()
    power_talk(H)