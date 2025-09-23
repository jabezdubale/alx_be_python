FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return((fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR)

def convert_to_fahrenheit(celsius):
    return((celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32)

temp_value = input("Enter the temperature to convert: ")
temp_type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

try:
    temp = float(temp_value)
    if temp_type == "C":
        fahrenheit_Value = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {fahrenheit_Value}°F")
    else:
        celsius_value = convert_to_celsius(temp)
        print(f"{temp}°F is {celsius_value}°C")
except:
    print("Invalid temperature. Please enter a numeric value.")