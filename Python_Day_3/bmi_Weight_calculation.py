bmi = float(input("Enter your BMI: "))

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal Weight")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obese")
