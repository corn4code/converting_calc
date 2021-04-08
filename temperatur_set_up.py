def Celsius_to_Kelvin(temperatur):
    global result
    result = temperatur + 273
    return result


def Celsius_to_Fahrenheit(temperatur):
    global result
    result = (temperatur * 1.8) + 32
    return result


def Kelvin_to_Celsius(temperatur):
    global result
    result = temperatur - 273
    return result

def Kelvin_to_Fahrenheit(temperatur):
    global result
    result = ((temperatur - 273) * 1.8) + 32
    return result
