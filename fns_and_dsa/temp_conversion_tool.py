FAHRENHEIT_TO_CELSIUS_FACTOR =5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR =9/5  # Ensures the exact match with regex

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = float(input("Enter the temperature to convert: "))
unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()  # Ensure consistency

if unit == "C":
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature:.2f}°C is {converted_temp:.2f}°F")  # Format output
elif unit == "F":
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature:.2f}°F is {converted_temp:.2f}°C")  # Format output
else:
    print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")  # Improved error handling