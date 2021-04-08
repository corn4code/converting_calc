import temperatur_set_up

choice = int(input("Choose your converter (enter assigned number):"
                   "1 Celsius to Kelvin, "
                   "2 Kelvin to Celsius"))

if choice == 1:
    teperatur = float(input("Enter temperature in Celsius: "))
    print(temperatur_set_up.Celsius_to_Kelvin(teperatur))

if choice == 2:
    temperatur = float(input("Enter temperature in Kelvin: "))
    print(temperatur_set_up.Kalvin_to_Celsius(temperatur))

else:
    print("invalid input")
