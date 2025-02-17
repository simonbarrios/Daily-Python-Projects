def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def celsius_to_kelvin(celsius):
    return celsius + 273.15

print("Temperature Converter")

input_temp = float(input("Enter the temperature: "))

while True:
    print("\nOptions:")
    print("Enter '1' to convert Celsius to Fahrenheit")
    print("Enter '2' to convert Fahrenheit to Celsius")
    print("Enter '3' to convert Kelvin to Celsius")
    print("Enter '4' to convert Celsius to Kelvin")
    print("Enter '5' to exit")
    input_option = input("Enter your choice: ")

    if input_option == '1':
        print(f"{input_temp}°C is {celsius_to_fahrenheit(input_temp)}°F")
        break
    elif input_option == '2':
        print(f"{input_temp}°F is {fahrenheit_to_celsius(input_temp)}°C")
        break
    elif input_option == '3':
        print(f"{input_temp}K is {kelvin_to_celsius(input_temp)}°C")
        break
    elif input_option == '4':
        print(f"{input_temp}°C is {celsius_to_kelvin(input_temp)}K")
        break
    elif input_option == '5':
        print("Exiting the program...")
        break
    else:
        print("Invalid option")
        
        
