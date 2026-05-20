# Store a temperature in Celsius as a float variable.
# Convert it to Fahrenheit using the formula:   F = (C × 9/5) + 32
# Convert it to Kelvin using the formula:       K = C + 273.15
# Print all three values, each rounded to 2 decimal places.
# Also print the type of the Celsius variable.
Celcius=32.00  
Fahrenheit = (Celcius *9/5)+32
Kelvin= Celcius+273.15

print(f"Fahrenheit: {Fahrenheit:.2f}\nKelvin: {Kelvin:.2f}\nType of Celsius: {type(Celcius)}")