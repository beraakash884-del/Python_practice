# Conditional Expresstion => A one line shortcut for if-else statements   (it is similer of ternary operator in c language)
# X if Confdition else Y

num = 0
print ("Positive" if num>=0 else "Negetive") 

result = "Even" if num % 2 == 0 else "Odd"
print(result) 

a=10
b=5
max_num = a if a>b else b
min_num = a if a<b else b
print(max_num)
print(min_num)