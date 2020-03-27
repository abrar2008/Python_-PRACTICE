#Function 
def Add_number():
    first_name  = 2 
    seocnd_number = 3
    total = first_name + seocnd_number 
   # print(total )


Add_number()

#Function Passed Value and Defulat Value 

def Add_number (first_name =0 , seocnd_number=0 ):
    total = first_name + seocnd_number 
    return total










 
ans = Add_number()

print(ans)



#File Handle

with open("data.txt" , "w") as f:
    f.write("Hello ,World")

