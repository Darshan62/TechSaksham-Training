# Write a program to simulate a coin toss using random module.
import random
for i in range(10):
    toss = random.randint(0,1)
    result = "Tail" if toss == 1 else "Head"
    print(result)