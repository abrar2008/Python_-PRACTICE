

def add(x , y ):
    return x + y 



def substract (x , y):
    return x - y 


def multiply (x,y):
    return x *y

def devide (x , y):
    return x/y

def power (x, y):
    return pow(x,y )


print("Select Operation ")
print("1 Add ")
print("2 Subtract")
print("3  Multiply")
print("4 Divide")
print("5 Power")

choice = input("Enter Choice (1/2/3/4/5)")

num1 = int (input("Enter First Number "))
num2 = int (input("Enter the Socond Number "))



if choice == '1':
    print(num1,  "+" , num2,"=" ,add(num1 , num2))

elif choice == '2':
    print(num1 , "-" , num2 , "=" , substract(num1, num2))
elif choice == '3':
    print(num1 , "*" , num2 , "=" , multiply(num1, num2))
elif choice == '4':
    print(num1 , "/" , num2 , "=" , devide(num1, num2))
elif choice == '5':
    print(num1 , "^" , num2 , "=" , power(num1, num2))
else :
    print("Invalid Input  ")



