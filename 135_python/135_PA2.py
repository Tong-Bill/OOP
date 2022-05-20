
x = input("How many pizzas are you considering ordering? ")
try:
    num_pizza = int(x)
except Exception:
    print("Invalid number of pizzas.")
    raise SystemExit

count = 1
Area1 = 0
Area2 = 0
cost1 = 0.00
cost2 = 0.00

while count <= num_pizza:
    y = input(f"Order {count}: What size is it, in inches? ")
    try:
        float(y)
    except Exception:
        print("Invalid size(inches).")
        raise SystemExit
    z = input("How much does this pizza cost? ")
    try:
        float(z)
    except Exception:
        print("Invalid price.")
        raise SystemExit

    # A = (pi)r^2
    r = float(y) / 2
    if count == 1:
        # Total pizza area
        Area1 = 3.14 * r * r
        # Cost pizza per inch
        cost1 = float(z)/Area1
    elif count == 2:
        Area2 = 3.14 * r * r
        cost2 = float(z)/Area2
    else:
        pass
    count += 1

if num_pizza == 2:
    if cost1 < cost2 and Area1 > Area2:
        print(f"Order 1 is the best choice @{cost1} with {Area1}in^2.")
    elif cost1 > cost2 and Area1 < Area2:
        print(f"Order 2 is the best choice @{cost2} with {Area2}in^2.")
    else:
        if cost1 > cost2:
            print("Order 1 has the lowest cost per inch.")
        elif cost1 < cost2:
            print("Order 2 has the lowest cost per inch.")
        else:
            print("Both orders have the same cost per inch.")

        if Area1 > Area2:
            print("Order 1 has the most overall area.")
        elif Area1 < Area2:
            print("Order 2 has the most overall area.")
        else:
            print("Both orders have the same overall area.")
else:
    print("Only one pizza was ordered.")
    raise SystemExit
