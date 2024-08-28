"""
Author: Benjamin Zeng
File name: Lab1.py
Description: Rock paper scissor
Date: Aug 28, 2024
"""

message = "go gators!"
print(message)

#Rock Paper Scissor Game below
import random

def rps():
    user = input("What will you use? \n")           #defining user as input and cpu to use random.
    cpu = random.choice(['rock','paper','scissor'])
    print()

    print('The user (you) chose', user)             #print what the user and comp will use.
    print('The cpu (I) chose', cpu)
    print()

    if user == cpu:                                 #if user and cpu use the same thing it will tie.
        print("Its a tie!!")

    if user == 'rock' and cpu == 'scissor':         #the outcome if user chose rock.
        print("rock beats scissor, user wins!")
    elif user == 'rock' and cpu == 'paper':
        print("paper beats rock, cpu wins!")

    if user == 'scissor' and cpu == 'paper':        #the outcome if user chose scissor
        print("scissor beats paper, user wins!")
    elif user == 'scissor' and cpu == 'rock':
        print("rock beats scissor, cpu wins")
    
    if user == 'paper' and cpu == 'rock':           #the outcome if user chose paper
        print("paper beats rock, user wins!")
    elif user == 'paper' and cpu == 'scissor':
        print("scissor beats paper, cpu wins")    
    
    print("Better luck next time!")
rps()
