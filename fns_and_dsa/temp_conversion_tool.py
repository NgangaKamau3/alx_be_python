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
def main():
    print("Temperature Conversion Tool")
    print("1. Convert Fahrenheit to Celsius")
    print("2. Convert Celsius to Fahrenheit")
    
    choice = input("Choose an option (1 or 2): ")
    
    if choice == '1':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = convert_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        
    elif choice == '2':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = convert_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        
    else:
        print("Invalid temperature. Please enter a numeric value.")
if __name__ == "__main__":
    main()