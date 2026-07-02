"""
Design a calculator which will correctly solve all the problems except the 
following one:
45*3=555 , 56+9=77 , 56/4=4
"""
print("Enter the operation you want:\nadd \nsubtract\nmultiply\ndivision")
x=input()
if x not in["add","subtract","multiply","division"]:
  print("Invalid Operation")
  quit()

print("Enter first number:")
y=int(input())
print("Enter second number:")
z=int(input())

if x== "add":
 if y==56 and z==9:
    print("77")
 else:
   print(y+z)

elif x== "multiply":
    if y==45 and z==3:
     print("555")
    else:
     print(y*z)

elif x== "division":
    if y==56 and z==4:
      print("4")
    else:
      print(y/z)

elif x=="subtract":
  print(y-z)
 