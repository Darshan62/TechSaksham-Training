#Write a program to input 3 numbers from user display the sum of non-duplicate 
#numbers. 

a,b,c =eval(input("Enter 3 numbers"))
if a==b and b==c:
    print("All are duplicates")
elif a==b :
    print("Sum : ",c)
elif b==c :
    print("Sum :",a)
elif a==c :
    print("Sum :",b)
else :
    print("Sum : ",a+b+c)