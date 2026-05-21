user_weight = int(input("What is your weight? \n"))
user_height = int(input("What is your height(in inches)? \n"))
weight = user_weight / 2.2
height = user_height / 39.2
print(weight)
print(height)

bmi = weight / height ** 2
print(round(bmi, 2))