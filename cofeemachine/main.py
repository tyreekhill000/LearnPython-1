MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
        "water": 300,
        "milk": 250,
        "coffee": 200,
        "money" :0
}

ACTION_OFF="OFF"
ACTION_REPORT="REPORT"
ACTION_ESPRESSSO="ESPRESSO"
ACTION_LATTE="LATTE"
ACTION_CAPPUCCINO="CAPPUCCINO"
ONE_QUARTER = 0.25
ONE_DIME = 0.10
ONE_NICKEL = 0.05
ONE_PENNY = 0.01



def printReport():
    print (f"Water :{resources['water']}")
    print (f"Milk :{resources['milk']}")
    print (f"Coffee :{resources['coffee']}")
    print (f"Money :{resources['money']}")

def getIngredient(action):
    if action==ACTION_ESPRESSSO.lower():
        return MENU["espresso"]["ingredients"]
    elif action==ACTION_LATTE.lower():
        return MENU["latte"]["ingredients"]
    elif action==ACTION_CAPPUCCINO.lower():
        return MENU["cappuccino"]["ingredients"]

    

def checkresource(ingredients,action):
    is_resource_avaliable=False
    if (ingredients["water"]>resources["water"]):
        print("Sorry there is not enough water")
    elif(ingredients["coffee"] >resources["coffee"]):
        print("Sorry there is not enough coffee")
    elif action==ACTION_ESPRESSSO.lower():
            is_resource_avaliable=True

    elif action==ACTION_LATTE.lower()  or  action==ACTION_CAPPUCCINO.lower():
        if ingredients["milk"] < resources["milk"]:
            is_resource_avaliable=True
        else :
            print("Sorry there is not enough milk")

    return  is_resource_avaliable

        
def processCoins(is_resource_avaliable):
    quarters=0
    dimes=0
    nickels=0
    pennies=0
    total=0
    if(not is_resource_avaliable):
        return total
    else:
        print("Please insert coins")
        quarters=int(input("How many quarters"))
        dimes=int(input("How many dimes"))
        nickels=int(input("How many nickels"))
        pennies=int(input("How many pennies"))
        total=(ONE_QUARTER*quarters)+(ONE_DIME*dimes)+(ONE_NICKEL*nickels)+(ONE_PENNY*pennies)     
        return total
    
def getCost(action):
    if action==ACTION_ESPRESSSO.lower():
        return MENU["espresso"]["cost"]
    elif action==ACTION_LATTE.lower():
        return MENU["latte"]["cost"]
    elif action==ACTION_CAPPUCCINO.lower():
        return MENU["cappuccino"]["cost"]
    
def processTransaction(total,cost):
    if total ==0:
        return False
    else:
        refund_amount=total-cost
        if(refund_amount >= 0):
            print(f"Here is ${round(refund_amount,2)} dollars in change")
            return True
        elif refund_amount <0:
            print(f"​Sorry that's not enough money. Money refunded.​")
            return False
def updateReport(action,ingredients,cost):
    resources["money"]+= cost
    resources["water"]-= ingredients["water"]
    resources["coffee"]-= ingredients["coffee"]
    if action==ACTION_LATTE.lower() or action==ACTION_CAPPUCCINO.lower():
        resources["milk"]-= ingredients["milk"]
     
def coffe_machine() :
    
    off_flag=True
    is_resource_avaliable=False
    isTransactionSuccessful=False
    action=input("​What would you like? (espresso/latte/cappuccino):")
    while off_flag ==True:
        if action ==ACTION_OFF.lower():
            off_flag=False
            return
        elif action==ACTION_REPORT.lower():
            printReport() 
        elif (action ==ACTION_CAPPUCCINO.lower() or action==ACTION_ESPRESSSO.lower() or action==ACTION_LATTE.lower()):
           ingredients= getIngredient(action)
           cost=getCost(action)
           is_resource_avaliable=checkresource(ingredients,action)
           total=processCoins(is_resource_avaliable)
           isTransactionSuccessful=processTransaction(total,cost)
           if(isTransactionSuccessful):
            print(f"Here is your {action}. Enjoy!")
            updateReport(action,ingredients,cost)  
        else: 
            print("Choose the correct option")
        
        action=input("​What would you like? (espresso/latte/cappuccino):")

coffe_machine()