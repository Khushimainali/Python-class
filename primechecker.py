#take integer N. Use nested loops or while to check if N is prime. Print yes/no

N= int(input("Enter a number :"))
is_prime = True

if N <= 1:
    is_prime = False
else:
    for i in range (2, int(N ** 0.5) +1):
        if N % i == 0:
            is_prime = False
            break
        if is_prime:
            print("Yes, Prime Number")
        else:
            print("No, Not a Prime Number")