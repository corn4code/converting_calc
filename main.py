import temperatur_set_up

print("Commands:")
print(" help: shows commands")
print(" overview: shows modules")
print(" list + module: lists modules functions ")
print(" use + module: lets you use the module")
print(" quit: end program")

while True:
    user_input = input(">> ")

    if user_input == "help":
        print("Commands:")
        print(" help: shows commands")
        print(" overview: shows modules")
        print(" list + module: lists modules functions ")
        print(" use + module: lets you use the module")
        print(" quit: end program")

    elif user_input == "overview":
        print("Modules:")
        print("  t: Temperature")

    elif user_input == "list t":
        print("Temperature ")
        print(" t1 Celsius to Kelvin")
        print(" t2 Celsius to Fahrenheit")
        print(" t3 Kelvin to Celsius")
        print(" t4 Kelvin to Fahrenheit")
        print(" t5 Fahrenheit to Celsius")
        print(" t6 Fahrenheit to Kelvin")

    elif user_input == "use t1":
        teperatur = float(input("Enter temperature in Celsius: "))
        print(temperatur, "°C =", temperatur_set_up.Celsius_to_Kelvin(teperatur), "K")

    elif user_input == "use t2":
        teperatur = float(input("Enter temperature in Celsius"))
        print(temperatur, "°C =", temperatur_set_up.Celsius_to_Fahrenheit(teperatur), "°F")

    elif user_input == "use t3":
        temperatur = float(input("Enter temperature in Kelvin: "))
        print(temperatur, "K =", temperatur_set_up.Kelvin_to_Celsius(temperatur), "°C")

    elif user_input == "use t4":
        temperatur = float(input("Enter temperature in Kelvin: "))
        print(temperatur, "K =", temperatur_set_up.Kelvin_to_Fahrenheit(temperatur), "°F")

    elif user_input == "use t5":
        temperatur = float(input("Enter temperature in Fahrenheit: "))
        print(temperatur, "°F =", temperatur_set_up.Fahrenheit_to_Celius(temperatur), "°C")

    elif user_input == "use t6":
        temperatur = float(input("Enter temperature in Fahrenheit: "))
        print(temperatur, "°F =", temperatur_set_up.Fahrenheit_to_Kelvin(temperatur), "°K")

    elif user_input == "quit":
        exit()

    else:
        print("invalid input")
