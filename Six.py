#Data FIle 

#Store data 
with open("data.txt" , "w")as f:
    f.write("Hello , World ")


#Retriving data 

with open ("data.txt" , "r") as f:
    text = f.read()
    print(text)

#Appending data


with open ("data.txt" , "a") as f:
    f.write("have a nice day ")


#Modules

import first

print(first.name)


#CSV FILE 
import csv
with open ("data.txt") as f :
    content = csv.reader(f)


#Reading Them CSV
import csv
with open ("data.txt") as f :
    content = csv.reader(f)
    pttter_competion = []
    for each_line in content f:
        pttter_competion += each _line 


#Picking informatin out of them 


target= input("Enter the name ")
index_number = potter_competion.index(target)
index_number =index_number _of_target 
potter_competion[index_number _of winner]
print("The winner was" + the_winner)


#Loading informaton into them  and Appending Rows to them 

import csv
with open ("data.txt" , "w" , newline="") as f :
    data_handler =csv.writer( f ,delattr=" " )
    data_handler.writerow(["1995" , "Event "])



#JSON 
import json
alpabet_letter = ["a" ,"b" , "c"]
with open ("data.json" ,"w" )as f:
    json.dump(alpabet_letter , f)


#Retrive 

import json
alpabet_letter = ["a" ,"b" , "c"]
with open ("data.json" ,"w" )as f:
    alpabet_letter = json.load(f)


#Try 

try:
    fielname = input("What istext fiel ")
    with open(fielname) as f:
        print(f.read)
except FileNotFoundError:
    print("Sorry " + fielname+ "Not found ")




