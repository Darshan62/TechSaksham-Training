# Pizza ordering program

print("Welcome to Python Pizza 🍕!")


size = input("Choose size (S, M, L): ").upper()
pepperoni = input("Do you want pepperoni? (Y/N): ").upper()
cheese = input("Do you want extra cheese? (Y/N): ").upper()


bill = 0
if size == "S":
    bill += 100
elif size == "M":
    bill += 200
elif size == "L":
    bill += 300


if pepperoni == "Y":
    bill += 30 if size == "S" else 50
if cheese == "Y":
    bill += 20

print(f"Your final bill is: ₹{bill}")
