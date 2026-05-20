# Q.1 Write a python program that:
#  Asks the user to enter a temperature in celcius
#  Convert it to Fahrenheit using the formula: F=(C*9/5)+32
#  Print the result in a clear formatted message.
temp = int(input("Enter temperature: "))
farenhite = (temp*9/5)+32
print(temp,"Degree Celcius Temperature to Farenhite : (",temp,"* 9 / 5 ) + 32 =", farenhite)