a=input("Enter your password :")

if(len(a)>8 & len(a)<16 & a.isalnum()):
    print("Correct password")
else:
     print("Your password should be minimum of 16 char & contain alphanumeric")