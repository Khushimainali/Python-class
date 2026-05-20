#print 1-50 for multiples of 3 prin Fizz , multiples of 5print Buzz , bot - FizzBuzz

for i in range(1, 51):
    if i % 3 == 0 and i % 5 ==0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
