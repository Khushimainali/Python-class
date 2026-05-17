
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