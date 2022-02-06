#Introduce and inquire
print("Cell Phone Bill")
print("________________________________")
add_mins = float(0)
add_texts = float(0)
mins = float(input("How many minutes did you use?-"))
texts = float(input("How many texts did you send?-"))
print("________________________________")
#Set conditions
if mins > 50:
    add_mins = round(((mins)-(50))*(0.25),2)
    print(f'Additional Minutes:\t${add_mins}')
if texts > 50:
    add_texts = round(((texts)-(50))*(0.15),2)
    print(f'Additional Texts:\t${add_texts}')
#Calculate and print
total_bill = round(((15)+(0.44)+(add_mins)+(add_texts))*(1.15),2)
emerg_fee = 0.44
base_charge = round((15)+(0.44)+(add_mins)+(add_texts),2)
tax = round((total_bill)-(base_charge),2)
print(f'Emergency Fee:\t\t${emerg_fee}')
print(f'Tax:\t\t\t${tax}')
print(f'Base Charge:\t\t${base_charge}')
print("________________________________")
print(f'Total Bill:\t\t${total_bill}')