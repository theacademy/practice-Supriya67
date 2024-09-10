import random
def dice_roller(n):
    r=[]
    for _ in range(n):
        result = random.randint(1,6)
        r.append(result)
    return r


n=int(input("enter the no. of dice you want? \n Minimum: 1 & Maximum: 6\n"))
if n>0 and n<7:
    print(dice_roller(n))
else:
    print("Enter a valid numbers")

