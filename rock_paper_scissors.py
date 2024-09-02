import random
def Game(Player_A):
    option=['stone','paper','scissors']
    Player_B=random.choice(option)
    print(f'Player_A {Player_A}\n Player_B {Player_B}')
    if (Player_A==Player_B):
        print("Tie")
    elif (Player_A=="stone"):
        if(Player_B=="paper" or Player_B=="scissors"):
            print("player_A won!!")
            print("Player_B lose -_-")
    elif(Player_A=="scissors"):
        if(Player_B=="paper"):
            print("player_A won!!")
            print("Player_B lose -_-")
        elif(Player_B=="stone"):
            print("Player_B win!!")
            print("Player_A lose -_-")
    elif(Player_A=="paper"):
        if(Player_B=="stone"):
            print("player_A won!!")
            print("Player_B lose -_-")
        elif(Player_B=="scissors"):
            print("Player_B win!!")
            print("Player_A lose -_-")
            
            

while True:
    print("input your choice\n press 1 for stone \n press 2 for paper \n press 3 for scissors")
    Choice=int(input())
    if (Choice<1 or Choice>3):
        print(" Enter a Invalid Choice")
    else:
        if Choice == 1:
            Player_A="stone"
        if Choice == 2:
            Player_A="paper"
        if Choice == 3:
            Player_A="scissors"
        Game(Player_A)
    print("Do you want to play again: \n press Y for Yes: \n perss N for No:")
    ans = input().upper()
    if ans == 'Y':
        continue
    else:
        break
print("thank you for playing!!")