def display_report(state):
    print(f'Water: {state["water"]}ml\nMilk: {state["milk"]}ml\nCoffee: {state["coffee"]}g\nMoney: ${state["money"]:.2f}')


def get_requirements(coffee_type):
    water_requirement = 0
    milk_requirement = 0
    coffee_requirement = 0
    money_requirement = 0

    if coffee_type == "espresso":
        water_requirement = 50
        coffee_requirement = 18
        money_requirement = 1.5
    elif coffee_type == "latte":
        water_requirement = 200
        milk_requirement = 150
        coffee_requirement = 24
        money_requirement = 2.5
    elif coffee_type == "cappuccino":
        water_requirement = 250
        milk_requirement = 100
        coffee_requirement = 24
        money_requirement = 3

    return {
        "water": water_requirement,
         "milk": milk_requirement,
         "coffee": coffee_requirement,
         "money": money_requirement
    }


def get_input():
    return input("What would you like? (espresso/latte/cappuccino): ").lower()


def validate_requirements(state, requirements): 
    if state["water"] < requirements["water"]:
        print("Sorry there is not enough water.")
        return False
    
    if state["milk"] < requirements["milk"]:
        print("Sorry there is not enough milk.")
        return False

    if state["coffee"] < requirements["coffee"]:
        print("Sorry there is not enough coffee.")
        return False

    return True

def get_money():
    print("Please insert coins.")

    num_quarters = int(input("How many quarters? "))
    num_dimes = int(input("How many dimes? "))
    num_nickles = int(input("How many nickles? "))
    num_pennies = int(input("How many pennies? "))

    return (0.25 * num_quarters) + (0.1 * num_dimes) + (0.05 * num_nickles) + (0.01 * num_pennies)


def process_input(user_input, state):
    if user_input == "report":
        display_report(state)
        return state
    
    valid_coffee_types = ["espresso", "latte", "cappuccino"]
    if not user_input in valid_coffee_types:
        print("Sorry! We don't have that.")
        return state

    requirements = get_requirements(user_input)
    if not validate_requirements(state, requirements):
        return state

    input_money = get_money()
    if input_money < requirements["money"]:
        print("Sorry that's not enough money. Money refunded.")
        return state
    elif input_money > requirements["money"]:
        change = input_money - requirements["money"]
        print(f"Here is ${change:.2f} in change.")

    new_state = {
        "water": state["water"] - requirements["water"],
        "milk": state["milk"] - requirements["milk"],
        "coffee": state["coffee"] - requirements["coffee"],
        "money": state["money"] + requirements["money"]
    }

    print(f"Here is your {user_input} ☕ Enjoy!")

    return new_state



if __name__ == "__main__":
    coffee_types = ["espresso", "latte", "cappuccino"]

    state = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0.0
    }

    user_input = get_input()

    while user_input != "off":
        state = process_input(user_input, state)
        user_input = get_input()

