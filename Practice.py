fullname= "Jeffrey Lionel Dahmer"
name= "Jeff or Dhamer"
age = 25
x= 10
print(f"My name is {fullname} and I'm {age} years old. But you can call me {name}")
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negetive")
else:
    print("x is zero")
for i in range(2):
    print(i)
names = ["Meshal","Enam","Rupom"]
for name in names:
    print(name)
s= set()
s.add(1)
s.add(2)
s.add(5)
s.add(3)
s.add(1)
s.remove(5)
print(s)
ages = {"Meshal":20,"Enam":21}
ages["Rupom"] = 21
ages["Meshal"] += 1
# ages["Meshal"] = ages["Meshal"] + 1
print(ages)
def square(x):
    return x*x
for i in range(10):
    print("{} squared is {}".format(i, square(i)))
    print(square(10))

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

p = Point(200, 300)
print(p.x)
print(p.y)