num = int(input("Enter the number :"))
list1 = []
i =2
while (i<num):
    if(num%i==0):
        list1.append(i)
    i=i+1
if not list1:
    print("Prime Number")
else:
    print(list1,"Not Prime ")