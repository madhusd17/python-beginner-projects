print("***************************************")
print("welcome to MY QUIZ game")
print("***************************************")
questions=[
    {'que':"The ability of one class to acquire methods and attributes of another class is called___.",'ans':"A"},
    {'que':"which of the following is a type of inheritance",'ans':"D"},
    {'que':"what type of inheritance has multiple subclasses to a single superclass?",'ans':"C"},
    {'que':"what is the depth of multilevel inheritance in python",'ans':"C"},
    {'que':"what does MRO stands for",'ans':"B"}
]
options=(["A.Inheritance","B.Abstraction","C.Polymorphism","D.Objects"],["A.single","B.Double","C.Multiple","D.both A&C"],["A.multiple inheritance","B.multilevel inheritance",
                                                                                                                           "C.heirarchical inheritance","D.none of these"],
         ["A.two level","B.three level","C.any level","D.none of these"],["A.method recursive object","B.method resolution order","C.main resolution order","D.method resolution object"])
count1=0
def check_answer(guess,correct_ans):
    if guess==correct_ans:
        print("Correct Answer")
        return True
    else:
        print("Incorrect Answer")
        print(f"correct answer is {questions[q]['ans']}")
        return False        
for q in range(len(questions)):
    print("***********************************************************************")
    print(questions[q]['que'])
    for i in options[q]:
        print(i)    
    answer=input("Enter your answer (A/B/C/D): ").upper()
    if answer not in ['A','B','C','D']:
       print("invalid choice!! please enter correct choice")
        #break
    is_correct=check_answer(answer,questions[q]['ans'])
    if is_correct==True:
        count1+=1
        print(f"your current score is {count1}/{len(questions)}")
    else:
        print(f"your current score is {count1}/5")
print("***********************************************************************************")
print(f"you have given {count1} correct answers")
print(f"your score is {count1/len(questions)*100}%")
print("***********************************************************************************")
     
