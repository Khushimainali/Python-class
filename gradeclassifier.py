# Write a Python program that:
# • Stores a student's marks (out of 100)
# • Checks if marks are >= 40  (pass condition)
# • Also checks if marks >= 75  (distinction)
# • Prints 'Distinction!' if >= 75, 'Pass' if >= 40, else 'Fail'
marks = 80

if marks >= 75:
    print("Distinction!")
elif marks >= 40:
    print("Pass")
else:
    print("Fail")