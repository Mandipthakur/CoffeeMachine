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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def enter_coin():
    """return total calculated from coins return"""
    print("Please insert coins.")
    total_cost=int(input("How many quartes?: "))*0.25

    total_cost+=int(input("how many dimes?: "))*0.1

    total_cost+=int(input("how many nickles?: "))*0.05

    total_cost += int(input("how many pennies?: "))*0.01

    return total_cost


def is_resources_sufficient(o_ingredients):
    for item in o_ingredients:
        if o_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough{item}.")
            return False
    return True


def is_trans_successful(money_received, drink_cost  ):
    if money_received>= drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here ${change} in change")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded. ")
        return False


def make_cofeee(drink_name,o_ingredients):
    """Duduct the required ingredients from the resources."""
    for item in o_ingredients:
        resources[item]-=o_ingredients[item]
    print(f"Here is your {drink_name}☕")



## TODO 1. ask for what they like to have
is_one =True
while is_one:
    user_choice = input("What would you like?(espresso/latte/cappuccino): ").lower()

    if user_choice == "report":
        print(f"Water:{resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif user_choice =="off":
        is_on=False
    else:
        drink=MENU[user_choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment= enter_coin()
            if is_trans_successful(payment,drink["cost"]):
                make_cofeee(user_choice,drink["ingredients"])





