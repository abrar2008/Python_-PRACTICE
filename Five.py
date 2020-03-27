#Function 

def add_numbers():
    first_number = 2
    second_number = 3 
    total = first_number +  second_number
    #print(total)






#Function Passing Them Information 

def two_number(first_number , second_number):
    total = first_number + second_number
    #print(total)


#two_number( 10   , 20)


#function ASSING default value 

def calo_tax(sales_total = 50 , tax_rate = 10):
    print(sales_total * tax_rate)

#calo_tax()    

greeting ("hello there" ,first_name = "dada")

def giver_greeting(greeting , first_name, flatering_nickname ="the  wonder boy "):
    print(greeting + " " + first_name + flatering_nickname)

#passing information  back from them 

def cal_tax (sales_total , tax_rate  ):
    return(sales_total * tax_rate)


#Function Local vs Global variables  


What_to_say = "hi"  # global variable 

def say_something():
    What_to_say = "hii"     #local variable 


 #Function with fiction 


def say_something():
    What_to_say = "hii"
    now_say() 




#While Loops

user_input = ""
while user_input != " q ":
    user_input = input("Enter a city ")
    if user_input !=q:




#Classes

class Patient():
    def __init__(self , last_name , first_name , age ):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age 
    def hello (self):
        if self.age < 20:
            print("This patientis a minor ")







     





