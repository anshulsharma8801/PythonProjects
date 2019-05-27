print("WELCOME TO THE GAME")
print("enter your name")
a=input()
print("guess a no. between 0-100")
num=int(input())
import random
r=random.randint(0,100)
i=0
j=0
while(i<5):
    if(r==num):
        print("CONGRATULATIONS")
        print("you guessed a correct no")
        j=1
    elif(r>num):
        print("guessed no is lower than the actual no")
        print("please guess again")
        num=int(input())
    else:
        print("guessed no is greater than actual no")
        print("please guess again")
        num=int(input())    
    i=i+1
if(j==1):
    print("your guess is correct")
else:
    print("better luck next time")

    
