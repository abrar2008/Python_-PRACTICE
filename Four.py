#tuples like list but this Fixed Elemennt 

state = ("Del " , "Alt"  , "New " , "Four ")



#print(state)

#Loop 

#for a in state:
 #   if state == : "dada"
  #      print("Welcome ")
   # else:
    #    print("Sorry ")

   #loop Nested 

first_name = ["Blue " , "upchuck" ,"lojack", "Gizmo" , ]
last_name =["khan" , "ali " ," maz" , "umsan "]

full_name = []

for a_firstname in first_name:
    for a_last_name in last_name:
        full_name.append(a_firstname + " " + a_last_name )
        break
        
#print(full_name)


#User Name 
a = input("Enter the name of a city ")  #input
a = a.lower()
a= a.upper()
a = a.title()
print(a)   #input




#Dictionaries 
list = ["Karachi  " , " Lahore " , "Multan"]   #List 



customer_8363 = {" first name" :"ibrar", "last name ": "Kahan " , "address " : "4803 well" }    
    # dic 

print(customer_8363)    
 # Add element 

customer_8363["city"] = "Karchi"

print(customer_8363)

#Removing 
del customer_8363["city"]

print(customer_8363)

#Looping 

for a in customer_8363.values():
    print( a)


#looping key
for a in customer_8363.keys():
    print(a)
    


    #loopi key and value


    for a , b in customer_8363.items():
        print("key "+a +" value " +b)


        #list of dictionariee

#
student [

            {
                "student_id": 0,
                "first name":"nasir ",
                "last name" :  "khan"
            },

            
            {
                "student_id": 1,
                "first name":"usman ",
                "last name" :  "khan"
            },
            
            
            {
                "student_id": 0,
                "first name":"ghaffar ",
                "last name"  :  "khan"
            }
            
        ]


        #New Lisr insert Diction 

new_diction= {
            "student_id": 5,
            "first name":"ibrar  ",
            "last name"  :  "k"

        }


student.append(new_diction)
print(student)


#Dictionary that contains list 

customer_8363 = {" first name" :"ibrar", "last name ": "Kahan " , "address " : "4803 well"  , "diccount" : ["standard" , "volme" , "lo"],}
print(customer_8363)    
