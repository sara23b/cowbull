#this program gets height and weight and gives the BMI and body condition

weight = float(input("Type in your Weight (kg):"))
height = float(input("Type in your Height (m):"))

BMI = weight/(height**2)

if BMI<=18.5:
    print ("Body weight deficit")
elif BMI>18.5 and BMI<=24:
    print ("Normal")
elif BMI>24 and BMI<=30:
    print ("Overweight")
elif BMI>30:
    print ("Obesity")

