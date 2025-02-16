# Write a program that generates a random password of user-specified length. 
#Program
import random
n=(int(input("Enter length of password")))
pas=""
for i in range (n):
    pas=pas+chr(random.randint(0,124))
print(pas)