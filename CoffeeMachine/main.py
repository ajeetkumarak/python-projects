MENU = {
    "espresso": {
        "ingredients": {
            "water": 100,
            "milk": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 34,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 34,
        },
        "cost": 4.0,
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def process_cost(order_cost):
    """Return the total calculated from coin inserted and make purchase"""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    total = quarters + dimes + nickles
    # print(f"${total}, {order_cost}")
    # print(earn_profit +
    global profit
    if total == order_cost:
        profit += order_cost
        return True
    elif total > order_cost:
        profit += order_cost
        print(f"you put extra money, here is your return ${round(total - order_cost, 2)}")
        return True
    else:
        print("Not sufficient , Money refunded  !!")
        return False


def report_resources(available_resources):
    for resource in available_resources:
        item_name = resource.title()
        item_quantity = available_resources[resource]
        print(f"{item_name}: {item_quantity}ml")
    print(f"Money: ${profit}")


def make_drink(drink_name, ingredients):
    for item in ingredients:
        left = resources[item] - ingredients[item]
        resources[item] = left

    return f"Here is your {drink_name}🍺 Enjoy!!"


def check_resources(order_items):
    is_enough = True
    for item in order_items:
        if order_items[item] >= resources[item]:
            print(f" Sorry, there is not enough {item}.")
            is_enough = False
    return is_enough

is_on = True
while is_on:
    order = input("What would you like? (espresso/latte/cappuccino)? or Type 'report' or 'off' : ")
    if order == "off":
        is_on = False
        print("Coffee machine is off.")
    elif order == 'report':
        report_resources(resources)
    else:
        order_items = MENU[order]["ingredients"]
        is_avilable = check_resources(order_items)
        if is_avilable:
            if process_cost(MENU[order]["cost"]):
                print(make_drink(order, order_items))
        else:
            is_on = False
            