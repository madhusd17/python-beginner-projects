import random
print("type 0 for rock,1 for paper,2 for scissor")
user_choice=int(input("enter your choice: "))
if user_choice>=3 or user_choice<0:
    print("you entered invalid number,you lose")
else:
    computer_choice=random.randint(0,2)
    print(f"computer choice:{computer_choice}")
    if computer_choice==user_choice:
          print("it's a draw")
    elif computer_choice==0 and user_choice==2:
        print("you lose")
    elif user_choice==0 and computer_choice==2:
        print("you win")
    elif computer_choice>user_choice:
        print("you lose")
    elif user_choice>computer_choice:
        print("you win")
    
        
