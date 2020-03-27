
#List 
city= ["karachi " , "lahore " , "Islamabad"]
print(city[1])
city.append("London")
print(city)

city.insert(2,"Sukkar")
print(city)

del city[1]
print(city)

city.remove("karachi")


last= city.pop(3)
print(city)