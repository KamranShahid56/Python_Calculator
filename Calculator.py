def add(x,y):
    return x+y
def minus(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y==0:
        print('Cannot be divided by zero')
    return (x/y)
print("Welcome to CODSOFT Internee's Calculator")
print("Chose which operation you want to perform:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
while True:
   choice=int(input("Select Operation: "))
   if choice in range(5):
      print("Enter Two Numbers")
      num1=float(input("Enter 1st number: "))
      num2=float(input("Enter 2nd number: "))
      if choice==1:
         print(num1,"+",num2,"=",add(num1,num2))
      if choice==2:
         print(num1,"-",num2,"=",minus(num1,num2))
      if choice==3:
         print(num1,"*",num2,"=",multiply(num1,num2))
      if choice==4:
         print(num1,"÷",num2,"=",divide(num1,num2))
   else:
      print('Invalid Input')
      exit()