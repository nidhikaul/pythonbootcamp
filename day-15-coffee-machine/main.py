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
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")
    
def process_coins():
    inserted_coins = (int(input("How many quarters?")) * 0.25)
    inserted_coins += (int(input("How many dimes?")) * 0.1)
    inserted_coins += (int(input("How many nickles?")) * 0.05)
    inserted_coins += (int(input("How many pennies?")) * 0.01)
    return inserted_coins

def cal_change(money_received, drink_cost):
    if money_received >= drink_cost:
        print(type(money_received))
        change = round(money_received - drink_cost, 2)
        print(f"Here is your change {change}") 
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

order_status = True
while order_status:
    order = input("What would you like? (espresso/latte/cappuccino):")
    if order == "off":
        order_status = False
    else:
        drink = MENU[order]
        print(drink)
        print("Please insert coins")
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins() 
            if cal_change(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])

    

    
    # inserted_coins = quarters + dimes + nickles + pennies
    # print(inserted_coins)
    # is_resource_suffiecient(drink["ingredients"])

    
    # if order == "espresso":
    #     menu[espresso[]
    # elif order == "latte":
    #     menu{latte}
    # elif order == "cappucino":
    #     menu{cappucino}
    # elif order == "report":
    #     print("{report}")
    # else:
    #     order_status = False



