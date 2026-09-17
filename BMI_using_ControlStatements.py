# BMI using FOR loop and IF,ELIF,ELSE
'''
n = int(input("Enter a no of times you want to check: "))
for i in range(n):
    name = input("enter your name: ")
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    if weight > 0 and height > 0:
        bmi = weight / height **2
        if bmi <= 18.5:
            print("{name} you are underweight")
        elif bmi <= 25 and bmi >= 18.5:
            print("{name} you are healthy")
        elif bmi <= 30 and bmi >= 25:
            print("{name} you are overweight")
        elif bmi >= 30:
            print("{name} are obese")
            if bmi >= 30 and bmi <= 35:
                print("{name} you have Type 1 obese")
            elif bmi >= 35 and bmi <= 40:
                print("{name} you have Type 2 obese")
            else :
                print("{name} you have obese Severe type")
    else:
        print("Enter positive real numbers")
'''
# BMI using For and WHILE LOOP:
n = int(input("Enter a no of times you want to check: "))
for i in range(n):
    while True:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        name = input("Enter your name: ")
        try:
            if weight > 0 and height > 0:
                bmi = weight / height **2
                if bmi <= 18.5:
                    print(f"{name} you are underweight")
                elif bmi <= 25 and bmi >= 18.5:
                    print("{name} you are healthy")
                elif bmi <= 30 and bmi >= 25:
                    print(f"{name} you are overweight")
                elif bmi >= 30:
                    print(f"{name} are obese")
                    if bmi >= 30 and bmi <= 35:
                        print(f"{name} you have Type 1 obese")
                    elif bmi >= 35 and bmi <= 40:
                        print(f"{name} you have Type 2 obese")
                    else:
                        print(f"{name} you have obese Severe type")

                break
            else:
                print("Enter positive real numbers")
                pass
        except Exception as e:
            print(f'Error is {e}')
