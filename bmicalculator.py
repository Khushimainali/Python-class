
# Q.3 Write a python program that:
# Asks the user for their name, weight(kg) and height(m)
# Calculates BMI using: BMI= weight/(height*height)
# Classifies: Underweight:(<18.5) | Normal(18.5-24.9) | Overweight(25-29.9) | Obese(> 3.0)

# Prints a personalized result: 'Hi[name]! BMI=[value] -- [category]'
name = input("Enter name : ")
weight = float(input("Enter weight : "))
height = float(input("Enter height : "))

bmi = weight / (height * height)

if bmi<18.5:
    category = "Underweight"

elif bmi>=18.5 or bmi<=24.9:
    category = "Normal"
    
elif bmi>=25 or bmi<=29.9:
    category = "Overweight"

else:
    category = "Obese"

print("Hi,",name,"\nBMI = ",bmi,"\ncategory = ",category)