# Write a program that takes a string as input and counts the occurrences of each character 
#in the string.

sentence = input("Enter a sentence: ")
char = input ("Type of character you want to count: ")

print(f"No of occurance of the {char} is {sum(1 for ch in sentence if ch == char)}")