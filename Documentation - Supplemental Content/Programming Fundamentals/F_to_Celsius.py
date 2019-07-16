def conv_2_C(fahrenheit):
    '''(number) -> float

    Return the number of celsius degrees equivalent to fahrenheit degrees.
    
    >>> Convert_to_celsius(32)
    0.0
    >>> Convert_to_celsius(212)
    100.0
    '''
    return (fahrenheit - 32) *5 / 9
def colder_temperature(temp1, temp2):
    '''(number, number) -> float
    Return the colder of the two temperatures, temp1 (degrees Celsius)
    and temp2 (degrees Fahrenheit), in degrees Celsius.
    '''
    temp2_celsius = conv_2_C(temp2)

    return min(temp1, temp2_celsius)



