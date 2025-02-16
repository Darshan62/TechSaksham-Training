#BMI Calculator
# BMI = weight (kg) / (height (m) * height (m))

weight = float(input("Enter your weight (kg): "))

bmi = weight / (height ** 2)


if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal weight"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print(f"Your BMI is {bmi:.2f}, which falls under '{category}'.")
