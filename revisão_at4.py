num1=int(input("digite um número: "))
num2=int(input("digite outro número: "))
num3=int(input("digite outro número: "))

if num1 > num2 and num1 >num3:
    print(f"o maior número é {num1}")
elif num2 > num3:
    print(f"o maior número é {num2}")
else:
    print(f"o maior número é {num3}")