#List 

city_0 = "karchi"
city_1 = "Lahore"
city_2 = "Sindth"


#print("Wellcome to " + city_0 )


#adding and changing element 



Cites = ["karachi " , "pakistan " ]

Cites.append("New york ")


#print(Cites)

Cites.insert( 0 , "london" )   # london , karachi  , pakistan  , new york 
#print(Cites[3])  #New York

# List Taking Slice Out Of Them 
cities =["Multon " , " karachi " , " lahore"]

smallest = cities[1]
#print(smallest)

#Lists Deleting And Removing Elements 

#cities =["Multon " , " karachi " , " lahore"]
    #     0               1            2

del cities[1]
print(cities)

cities.remove("lahore")
print(cities)


#Lists Popping Eement 

cities =["Multon " , " karachi " , " lahore"]
lastest = cities.pop(1)
print(lastest)
