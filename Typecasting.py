#Today we will be learing about type casting in  python
# To type cast a variable or a value in a certain veriable all you need to do is data_type(value or veriable)
#Like this int(), str(), flaot(), bool()
#To get the data type of a verable => type(value or verable)

 #string
name="zero"
#int
age=20
#float
salery=0.00
#boolean 
is_student=True;
# to get the data type
print(type(name))
print(type(age))
print(type(salery))
print(type(is_student))
#Typecast
salery=int(salery)  #float to int 
print(salery)
age=float(age)
print(age)   #int to float
name="1"  # but we can convert "1" type of string into int float
name=int(name)  #we can't convert zero string into an int 
print(name)

name="zero"
name=bool(name)
print(name)   # it will print True
name="" #now name string is empty 
name=bool(name)
print(name)  # now it will print false beacuse name veriable contain empty string.

is_student=str(is_student)
print(is_student)