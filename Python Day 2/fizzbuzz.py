# Write a program that prints numbers from 0 to 100. For multiples of 3, print 'Fizz' instead 
#of the number, for multiples of 5, print 'Buzz', and for numbers that are multiples of both 3 
#and 5, print 'FizzBuzz'.
for num in range (1,101):
    if (num%3==0 and num%5!=0):
        print("Fizz")
    elif (num%5==0 and num%3!=0):
        print("Buzz")
    elif (num%3==0 and num%5==0):
        print("Fizz Buzz")
    else:
         print(num)