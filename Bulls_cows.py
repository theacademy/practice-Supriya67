import random
def bull_cows(secret_num,guess):
    bull_cows=[0,0]
    secret_num_list=getDigit(secret_num)
    guess_list=getDigit(guess)
    for i,j in zip(secret_num_list,guess_list):
        if j in secret_num_list:
            if j==i:
                bull_cows[0] += 1
            else:
                bull_cows[1] += 1
    return bull_cows
        
    
    
def getDigit(n):
    return([int(x) for x in str(n)])
    
def noDuplicate(a):
    b=getDigit(a)
    if len(b)==len(set(b)):
        return True
    else:
        return False
    

def secret_num1():
    while True:
        a=random.randint(1000,9999)
        if noDuplicate(a):
            return a
    

secret_num=secret_num1()
print(secret_num)

tries =int(input('Enter number of tries: ')) 
while tries>0:
    guess=int(input('Enter your guess: '))
    if not noDuplicate(guess):
        print("invalid")
    B_C=bull_cows(secret_num,guess)
    if B_C[0] == 4:
        print("you are right")
        break
    tries-=1
else:
    print("You ran out of tries")