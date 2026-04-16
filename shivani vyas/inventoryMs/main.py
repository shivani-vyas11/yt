# Inventory Management System using Dictionary

inventory = {
    "Laptop": {"price": 60000, "quantity": 10},
    "Keyboard": {"price": 800, "quantity": 50},
    "Mouse": {"price": 500, "quantity": 40}
}

def view_inventory():
    print("\n----- INVENTORY LIST -----")
    if not inventory:
        print("Inventory is empty.")
    for item, details in inventory.items():
        print(f"Item: {item}, Price: ₹{details['price']}, Quantity: {details['quantity']}")

def add_item():
    name = input("Enter item name: ")
    if name in inventory:
        print("Item already exists!")
    else:
        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        inventory[name] = {"price": price, "quantity": quantity}
        print("Item added successfully.")

def update_stock():
    name = input("Enter item name to update stock: ")
    if name in inventory:
        quantity = int(input("Enter quantity to add: "))
        inventory[name]["quantity"] += quantity
        print("Stock updated successfully.")
    else:
        print("Item not found.")

def sell_item():
    name = input("Enter item name to sell: ")
    if name in inventory:
        quantity = int(input("Enter quantity to sell: "))
        if inventory[name]["quantity"] >= quantity:
            inventory[name]["quantity"] -= quantity
            print("Item sold successfully.")
            if inventory[name]["quantity"] == 0:
                print(f"{name} is out of stock.")
        else:
            print("Not enough stock.")
    else:
        print("Item not found.")

def remove_item():
    name = input("Enter item name to remove: ")
    if name in inventory:
        del inventory[name]
        print("Item removed successfully.")
    else:
        print("Item not found.")

while True:
    print("\n===== INVENTORY MANAGEMENT SYSTEM =====")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Update Stock")
    print("4. Sell Item")
    print("5. Remove Item")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        view_inventory()
    elif choice == "2":
        add_item()
    elif choice == "3":
        update_stock()
    elif choice == "4":
        sell_item()
    elif choice == "5":
        remove_item()
    elif choice == "6":
        print("Exiting Inventory Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")