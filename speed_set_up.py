#start kph
def kph_to_mph(speed): #to miles per hour
    global result
    result = speed / 1.609344
    return result


def kph_to_mps(speed): #to meters per second
    global result
    result = speed / 3.6
    return result


def kph_to_knot(speed):
    global result
    result = speed / 1.852
    return result


def kph_to_fps(speed): #feet per second
    global result
    result = speed / 1.09728
    return result
# end kph

# start mph
def mph_to_kph(speed):
    global result
    result = speed * 1.609344
    return result

def mph_to_mps(speed):
    global result
    result = speed * 2.23693629
    return result

def mph_to_knots(speed):
    global result
    result = speed * 1.15077945
    return result

def mph_to_fps(speed):
    global result
    result = speed * 1.46666667
    return result
# end mph
# start mps
def mps_to_kph(speed):
    global result
    result = speed * 3.6
    return result

def mps_to_mph(speed):
    global result
    result = speed * 2.23693629
    return result

def mps_to_knots(speed):
    global result
    result = speed * 1.94384449
    return result

def mps_to_fps(speed):
    global result
    result = speed * 3.2808399
    return result
