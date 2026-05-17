# Write a Python program that simulates a basic ATM:
# • Stores balance = 5000 and withdrawal amount = 2000
# • Checks: amount > 0  AND  amount <= balance  (valid withdrawal)
# • If valid: subtract amount, print new balance
# • If amount > balance: print 'Insufficient funds'
# • BONUS: also check if amount % 100 == 0 (ATM only gives multiples of 100
balance = 5000
amount = 2000

if amount > 0 and amount <= balance and amount % 100 == 0:
    balance -= amount
    print("Withdrawal successful!")
    print("New balance: NPR", balance)
elif amount > balance:
    print("Insufficient funds")
else:
    print("Invalid amount")