# Define functions to convert temperatures between Celsius and Fahrenheit
# Define global variables for the conversion factors

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#Conversion from Fahrenheit to Celsius
def convert_to_celsius(fahrenheit):
    """
    Function to convert temperature from Fahrenheit to celsius.
    Input:
        - fahrenheit: Temperature in Fahrenheit (float or int)(User input)

    Returns:
        - Temperature in Celsius (float) 

    """
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

#Conversion from Celsius to Fahrenheit
def convert_to_fahrenheit(celsius):
    """
    Function to convert temperature from Celsius to Fahrenheit.
    Input:
        - celsius: Temperature in Celsius (float or int)(User input)
    Returns:
        - Temperature in Fahrenheit (float)
    """
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

#Wrapping it all together in a main function and providing user interaction
# Example usage:
# Enter the temperature to convert: 0
# Is this temperature in Celsius or Fahrenheit? (C/F): C
# 0.0°C is 32.0°F
def main():
    temp_input = float(input("Enter the temperature to convert: "))
    scale = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if scale == 'C':
        converted_temp = convert_to_fahrenheit(temp_input)
        print(f"{temp_input}°C is {converted_temp}°F")
    elif scale == 'F':
        converted_temp = convert_to_celsius(temp_input)
        print(f"{temp_input}°F is {converted_temp}°C")
    else:
        print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()