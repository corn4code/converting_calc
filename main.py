import temperatur_set_up

def get_input():
    global input
    input("enter command: ")
    return input

print("Commands:")
print(" help: shows commands")
print(" overview: shows conversion modules")
print(" option + module abbreviation: shows details to conversions")
print(" quit(): end program")

while True:
    input = input(">> ")
    # get_input()
    if input == "help":
        print("Commands:")
        print(" help: shows commands")
        print(" overview: shows conversion modules")
        print(" option + module abbreviation")

    elif input == "overview":
        print("Modules:")
        print("  t: Temperature")

    elif input == "option t":
        print("Temperature ")
        print("  t1 Celsius to Kelvin")
        print("  t2 Celsius to Fahrenheit")
        print("  t3 Kelvin to Celsius")
        print("  t4 Kelvin to Fahrenheit")
        print("  t5 Fahrenheit to Celsius")
        print("  t6 Fahrenheit to Kelvin")

    elif input == "t1":
        teperatur = float(input("Enter temperature in Celsius: "))
        print(temperatur_set_up.Celsius_to_Kelvin(teperatur))

    elif input == "t2":
        teperatur = float(input("Enter temperature in Celsius"))
        print(temperatur_set_up.Celsius_to_Fahrenheit(teperatur))

    elif input == "t3":
        temperatur = float(input("Enter temperature in Kelvin: "))
        print(temperatur_set_up.Kelvin_to_Celsius(temperatur))

    elif input == "t4":
        temperatur = float(input("Enter temperature in Kelvin: "))
        print(temperatur_set_up.Kelvin_to_Fahrenheit(temperatur))

    elif input == "t5":
        temperatur = float(input("Enter temperature in Fahrenheit: "))
        print(temperatur_set_up.Fahrenheit_to_Celvin(temperatur))

    elif input == "t6":
        temperatur = float(input("Enter temperature in Fahrenheit: "))
        print(temperatur_set_up.Fahrenheit_to_Kelvin(temperatur))

    elif input == "quit()":
        break

    else:
        print("invalid input")
