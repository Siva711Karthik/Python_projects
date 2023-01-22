Height = input("Enter the user height in centimeters:")
Weight = input("Enter the user weight in killograms:")
Height = float(Height)
Weight = float(Weight)
BMI = (Weight/Height**2)*10000
print(f"the value of BMI",BMI)
if BMI >=30:
    print("BMI indicates obesity")
elif BMI >25 and BMI<29:
    print("BMI indicates overweight")
elif BMI >18.5 and BMI <25:
    print("BMI indicates normal")
else:
    print("BMI indicates underweight")




