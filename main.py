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
# print("Overview: ")
# print("  t: Temperature ")
# print("    t1 Celsius to Kelvin")
# print("    t2 Celsius to Fahrenheit")
# print("    t3 Kelvin to Celsius")
# print("    t4 Kelvin to Fahrenheit")
while True:
    input = str(input("enter command: "))
    # get_input()
    if input == "help":
        print("Commands:")
        print(" help: shows commands")
        print(" overview: shows conversion modules")
        print(" option + module abbreviation")

    if input == "overview":
        print("Modules:")
        print("  t: Temperature")

    if input == "option t":
        print("Temperature ")
        print("  t1 Celsius to Kelvin")
        print("  t2 Celsius to Fahrenheit")
        print("  t3 Kelvin to Celsius")
        print("  t4 Kelvin to Fahrenheit")



    # choice = input

    if input == "t1":
        teperatur = float(input("Enter temperature in Celsius: "))
        print(temperatur_set_up.Celsius_to_Kelvin(teperatur))

    if input == "t2":
        teperatur = float(input("Enter temperature in Celsius"))
        print(temperatur_set_up.Celsius_to_Fahrenheit(teperatur))

    if input == "t3":
        temperatur = float(input("Enter temperature in Kelvin: "))
        print(temperatur_set_up.Kelvin_to_Celsius(temperatur))

    if input == "t4":
        temperatur = float(input("Enter temperature in Kelvin: "))
        print(temperatur_set_up.Kelvin_to_Fahrenheit(temperatur))

    if input == "quit()":
        break

