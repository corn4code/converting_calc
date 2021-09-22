import temperatur_set_up
import speed_set_up

print("Commands:")
print(" help: shows commands")
print(" overview: shows modules")
print(" list + module: lists modules functions ")
print(" use + module: lets you use the module")
print(" exit: end program")

while True:
    user_input = input(">> ")

    if user_input == "help":
        print("Commands:")
        print(" help: shows commands")
        print(" overview: shows modules")
        print(" list + module: lists modules functions ")
        print(" use + module: lets you use the module")
        print(" exit: end program")

    elif user_input == "overview":
        print("Modules:")
        print("  t: Temperature")
        print("  s: Speed")

# start temperature
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
        print(teperatur, "°C =", temperatur_set_up.Celsius_to_Kelvin(teperatur), "K")

    elif user_input == "use t2":
        teperatur = float(input("Enter temperature in Celsius"))
        print(teperatur, "°C =", temperatur_set_up.Celsius_to_Fahrenheit(teperatur), "°F")

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

# end temperature

# start speed

    elif user_input == "list s":
        print("Speed:")
        print(" s1 kph to")
        print(" s2 mph to")
        print(" s3 mps to")
        print(" s4 knots to")
        print(" s5 feet per second to")

    # start kph
    elif user_input == "list s1":
        print("Speed in kph")
        print(" s1a kph to mph")
        print(" s1b kph to mps")
        print(" s1c kph to knots")
        print(" s1d kph to fps")

    elif user_input == "use s1a":
        speed = float(input("enter speed in kph: "))
        print(speed, "kph =", speed_set_up.kph_to_mph(speed), "mph")

    elif user_input == "use s1b":
        speed = float(input("enter speed in kph: "))
        print(speed, "kph =", speed_set_up.kph_to_mps(speed), "mps")

    elif user_input == "use s1c":
        speed = float(input("enter speed in kph: "))
        print(speed, "kph =", speed_set_up.kph_to_knot(speed), "knots")

    elif user_input == "use s1d":
        speed = float(input("enter speed in kph: "))
        print(speed, "kph =", speed_set_up.kph_to_fps(speed), "fps")
    # end kph
    # start mph
    elif user_input == "list s2":
        print("Speed in mph")
        print(" s2a mph to kph")
        print(" s2b mph to mps")
        print(" s2c mph to knots")
        print(" s2d mph to fps")

    elif user_input == "use s2a":
        speed = float(input("enter speed in mph: "))
        print(speed, "mph = ", speed_set_up.mph_to_kph(speed), "kph")

    elif user_input == "use s2b":
        speed = float(input("enter speed in mph: "))
        print(speed, "mph =", speed_set_up.mph_to_mps(speed), "mps")

    elif user_input == "use s2c":
        speed = float(input("enter speed in mph: "))
        print(speed, "mph = ", speed_set_up.mph_to_knots(speed), "knots")

    elif user_input == "use s2d":
        speed = float(input("enter speed in mph: "))
        print(speed, "mph = ", speed_set_up.mph_to_fps(speed), "fps")
    # end mph
    # start mps
    elif user_input == "list s3":
        print("Speed in mps")
        print(" s3a mps to kph")
        print(" s3b mps to mph")
        print(" s3c mps to knots")
        print(" s3d mps to fps")

    elif user_input == "use s3a":
        speed = float(input("enter speed in mps: "))
        print(speed, "mps = ", speed_set_up.mps_to_kph(speed), "kph")

    elif user_input == "use s3b":
        speed = float(input("enter speed in mps: "))
        print(speed, "mps = ", speed_set_up.mps_to_mph(speed), "mph")

    elif user_input == "use s3c":
        speed = float(input("enter speed in mps: "))
        print(speed, "mps = ", speed_set_up.mps_to_knots(speed), "knots")

    elif user_input == "use s3d":
        speed = float(input("enter speed in mps: "))
        print(speed, "mps = ", speed_set_up.mps_to_fps(speed), "fps")
    # end mps

# end speed

    elif user_input == "exit":
        exit()

    else:
        print("invalid input")
