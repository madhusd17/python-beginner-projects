import random
print("let me think of a number between 1 to 50")
level=input("choose level of difficulty type 'easy' or 'difficult': ")
attempts=0
if level=='easy':
    attempts=10
elif level=='difficult':
    attempts=5
else:
    print("invalid choice")
sys_choice=random.randint(1,50)
print(sys_choice)

for i in range(attempts,0,-1):
    print(f"you have {i} attempts remaining to guess the number!")
    user_choice=int(input("make a guess:"))
    if user_choice==sys_choice:
        print("you won")
        break
    elif user_choice>sys_choice:
        print("your guess is too high")
    elif user_choice<sys_choice:
        print("your choice is too low")
else:
    print("you lose")


