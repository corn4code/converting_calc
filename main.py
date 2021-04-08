import temperatur_set_up

print("Overview: ")
print("Temperature: ")
print("    t1 Celsius to Kelvin")
print("    t2 Celsius to Fahrenheit")
print("    t3 Kelvin to Celsius")
print("    t4 Kelvin to Fahrenheit")

choice = input("Choose your converter (enter abbrevation assigned in overview:")

if choice == "t1":
    teperatur = float(input("Enter temperature in Celsius: "))
    print(temperatur_set_up.Celsius_to_Kelvin(teperatur))

if choice == "t2":
    teperatur = float(input("Enter temperature in Celsius"))
    print(temperatur_set_up.Celsius_to_Fahrenheit(teperatur))

if choice == "t3":
    temperatur = float(input("Enter temperature in Kelvin: "))
    print(temperatur_set_up.Kelvin_to_Celsius(temperatur))

if choice == "t4":
    temperatur = float(input("Enter temperature in Kelvin: "))
    print(temperatur_set_up.Kelvin_to_Fahrenheit(temperatur))

else:
    print("invalid input")
