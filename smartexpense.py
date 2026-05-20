# You went on a trip with 4 friends. Store the following as variables:
#   • total_bill = 3750.00 (float)    • num_people = 5 (int)    • paid_extra = True (bool)
#   • discount_percent = 10 (int)     • your_name = 'Arjun' (str)
# Calculate and print:
#   1. Bill after discount    2. Each person's share (2 decimal places)    3. Type of each variable
total_bill = 3750.00
num_people = 5
paid_extra = True
discount_percent = 10
your_name = "Arjun"

bill_after_discount = total_bill - (total_bill * discount_percent / 100)

print("Bill after discount:", bill_after_discount)
print("Each person's share:", round(bill_after_discount / num_people, 2))

print(type(total_bill))
print(type(num_people))
print(type(paid_extra))
print(type(discount_percent))
print(type(your_name))