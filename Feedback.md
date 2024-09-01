Supriya,

Code looked well organized and well thought out.  Bulls and cows had one minor issue with feedback after a guess, there was none.
RPS worked great. No issues,  except after I gave an invalid input.  The app tried to recover, then crashed.  Take a look at my error message:

CONSOLE OUTPUT:
```
input your choice
 press 1 for stone
 press 2 for paper
 press 3 for scissors
7
 Enter a Invalid Choice
Do you want to play again:
 press Y for Yes:
 perss N for No:
Y
input your choice
 press 1 for stone
 press 2 for paper
 press 3 for scissors
2
Traceback (most recent call last):
  File "C:\Users\dhunnicutt\Desktop\Practice Python C398\test.py", line 41, in <module>
    Game(Player_A)
NameError: name 'Player_A' is not defined. Did you mean: 'Player_B'?```
PS C:\Users\dhunnicutt\Desktop\Practice Python C398>
