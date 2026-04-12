l=50
c=100
e=150
menu={
    "water":150,
    "milk":160,
    "coffee":60,
    "money":0
}
    
is_true=True
while is_true:
    user_choice=input("what would you like to have?(latte(l)/espresso(e)/cappuccino(c)):")
    if user_choice=='report':
        print(menu)
    elif user_choice=='off':
        is_true=False
    elif user_choice=='c' or 'l' or 'e':
        if menu['water']>=50 and menu['milk']>=80 and menu['coffee']>=10:
            print("resources are available")
            sum=0
            rs5=int(input("enter number of 5Rs coins:"))
            rs10=int(input("enter number of 10Rs coins:"))
            rs20=int(input("enter number of 20Rs coins:"))
            sum=(5*rs5)+(10*rs10)+(20*rs20)
        
            if user_choice=='l':
                if sum==l:
                    print("take ur coffee")
                elif sum<l:
                    print("insufficient coins")
                    continue
                else:
                    print(f"take {sum-l}Rs change and have ur coffee")
                menu['money']+=l
                menu['water']-=50
                menu['coffee']-=10
            elif user_choice=='c':
                if sum==c:
                    print("take ur coffee")
                elif sum<c:
                    print("insufficient coins")
                    continue
                else:
                    print(f"take {sum-c} rs change and have ur coffee")
                menu['money']+=c
                menu['water']-=50
                menu['coffee']-=10
                menu['milk']-=30
            elif user_choice=='e':

                if sum==e:
                    print("take ur coffee")
                elif sum<e:
                    print("insufficient coins")
                    continue
                else:
                    print(f"take {sum-e}Rs change and have ur coffee")
                menu['money']+=e
                menu['coffee']-=10
                menu['milk']-=80
            
        else:
            print("insufficient resources")
            
    
        
             
