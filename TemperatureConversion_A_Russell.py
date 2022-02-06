#title
print("Temperature Conversion:")
print("_______________________")
print()
#get input from user
celsius= float(input("What's the temperature?: "))

#calculate results
fahrenheit=round((((celsius)*(1.8))+32),2)
kelvin=round((celsius)+(273.15),2)


#print results
print(f'Celsius:{celsius} degrees ')
print(f'Fahrenheit:{fahrenheit} degrees')
print(f'Kelvin:{kelvin} degrees')
