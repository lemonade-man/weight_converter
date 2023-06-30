weight = int(input("your weight: "))
unit = input("(k)g or (L)bs: ").lower()
if unit == "k":
    print(str(weight / 0.45) + "Lb")
else:
    print(str(weight * 0.45) + "Kg")
