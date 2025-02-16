# Write a program to display sum of all even numbers from 1 to 100.
sum1=0
for i in range(0,101):
    if (i%2 ==0):
        sum1+=i
print(sum1)
print(sum(list(range(2,101,2))))