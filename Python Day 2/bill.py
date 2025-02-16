#Write a program that randomly selects a person from a given list of names to pay the bill. 
#Program : 
import random 
names_string = input("Enter the  names seprated by comma and space : ")
names = names_string.split(",")

random_ind = random.randint(0,len(names)-1)
payer = names[random_ind]
print(f"{payer} is going to pay the bill !")
