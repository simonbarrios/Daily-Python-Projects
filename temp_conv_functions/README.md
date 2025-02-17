# Temperature Converter

A simple command-line temperature conversion program that allows users to convert temperatures between Celsius, Fahrenheit, and Kelvin scales.

## Features

- Convert Celsius to Fahrenheit
- Convert Fahrenheit to Celsius
- Convert Kelvin to Celsius
- Convert Celsius to Kelvin

## Functions

### `celsius_to_fahrenheit(celsius)`

Converts a temperature from Celsius to Fahrenheit

- Input: Temperature in Celsius (float)
- Output: Temperature in Fahrenheit (float)
- Formula: °F = (°C × 9/5) + 32

### `fahrenheit_to_celsius(fahrenheit)`

Converts a temperature from Fahrenheit to Celsius

- Input: Temperature in Fahrenheit (float)
- Output: Temperature in Celsius (float)
- Formula: °C = (°F - 32) × 5/9

### `kelvin_to_celsius(kelvin)`

Converts a temperature from Kelvin to Celsius

- Input: Temperature in Kelvin (float)
- Output: Temperature in Celsius (float)
- Formula: °C = K - 273.15

### `celsius_to_kelvin(celsius)`

Converts a temperature from Celsius to Kelvin

- Input: Temperature in Celsius (float)
- Output: Temperature in Kelvin (float)
- Formula: K = °C + 273.15

## Usage

1. Run the program
2. Enter a temperature value when prompted
3. Choose a conversion option (1-5):
   - Option 1: Celsius to Fahrenheit
   - Option 2: Fahrenheit to Celsius
   - Option 3: Kelvin to Celsius
   - Option 4: Celsius to Kelvin
   - Option 5: Exit program
4. View the converted temperature result

The program will display the result and exit after performing one conversion.
