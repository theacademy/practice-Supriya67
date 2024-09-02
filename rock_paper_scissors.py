{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "def Game(Player_A):\n",
    "    option=['stone','paper','scissors']\n",
    "    Player_B=random.choice(option)\n",
    "    print(f'Player_A {Player_A}\\n Player_B {Player_B}')\n",
    "    if (Player_A==Player_B):\n",
    "        print(\"Tie\")\n",
    "    elif (Player_A==\"stone\"):\n",
    "        if(Player_B==\"paper\" or Player_B==\"scissors\"):\n",
    "            print(\"player_A won!!\")\n",
    "            print(\"Player_B lose -_-\")\n",
    "    elif(Player_A==\"scissors\"):\n",
    "        if(Player_B==\"paper\"):\n",
    "            print(\"player_A won!!\")\n",
    "            print(\"Player_B lose -_-\")\n",
    "        elif(Player_B==\"stone\"):\n",
    "            print(\"Player_B win!!\")\n",
    "            print(\"Player_A lose -_-\")\n",
    "    elif(Player_A==\"paper\"):\n",
    "        if(Player_B==\"stone\"):\n",
    "            print(\"player_A won!!\")\n",
    "            print(\"Player_B lose -_-\")\n",
    "        elif(Player_B==\"scissors\"):\n",
    "            print(\"Player_B win!!\")\n",
    "            print(\"Player_A lose -_-\")\n",
    "            \n",
    "            \n",
    "\n",
    "while True:\n",
    "    print(\"input your choice\\n press 1 for stone \\n press 2 for paper \\n press 3 for scissors\")\n",
    "    Choice=int(input())\n",
    "    if (Choice<1 or Choice>3):\n",
    "        print(\" Enter a Invalid Choice\")\n",
    "    else:\n",
    "        if Choice == 1:\n",
    "            Player_A=\"stone\"\n",
    "        if Choice == 2:\n",
    "            Player_A=\"paper\"\n",
    "        if Choice == 3:\n",
    "            Player_A=\"scissors\"\n",
    "        Game(Player_A)\n",
    "    print(\"Do you want to play again: \\n press Y for Yes: \\n perss N for No:\")\n",
    "    ans = input().upper()\n",
    "    if ans == 'Y':\n",
    "        continue\n",
    "    else:\n",
    "        break\n",
    "print(\"thank you for playing!!\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
