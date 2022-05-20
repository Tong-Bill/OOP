

count = 1

while True:
    try:
        num_orders = int(input("Welcome to McKeith's! How many orders do you have? "))
        break
    except Exception:
        print("Input was not an integer. Please try again.")

while count <= num_orders:
    x, y, z = input(f"Order {count} (combo# size price): ").split()
    try:
        int(x)
    except Exception:
        print("Invalid integer for combo#")
        break

    y = y.upper()
    if y == "S" or y == "M" or y == "L":
        pass
    else:
        print("Invalid size. Choose S for small, M for medium, L for large.")
        break

    try:
        float(z)
    except Exception:
        print("Invalid float for price")
        break

    print(x, y, z)
    count += 1
