import os

# Function to create or update the inventory file
def update_inventory(item, quantity, inventory_file):
    inventory = {}
    if os.path.exists(inventory_file):
        with open(inventory_file, 'r') as f:
            for line in f:
                item_name, stock = line.strip().split(',')
                inventory[item_name] = int(stock)

    if item in inventory:
        if inventory[item] >= quantity:
            inventory[item] -= quantity
        else:
            return False  # Item is out of stock
    else:
        return False  # Item not found in inventory

    with open(inventory_file, 'w') as f:
        for item_name, stock in inventory.items():
            f.write(f"{item_name},{stock}\n")

    return True

# Function to generate a bill
def generate_bill(cart, inventory_file, output_file):
    total_price = 0
    out_of_stock_items = []

    with open(output_file, 'w') as f:
        f.write("Item,Quantity,Price\n")
        for item, quantity, price_per_item in cart:
            if update_inventory(item, quantity, inventory_file):
                item_total = quantity * price_per_item
                total_price += item_total
                f.write(f"{item},{quantity},${item_total:.2f}\n")
            else:
                out_of_stock_items.append(item)

    return total_price, out_of_stock_items

# Example usage
cart = [("Item1", 2, 5.99), ("Item2", 3, 2.49)]
inventory_file = "inventory.txt"
output_file = "bill.txt"

total_price, out_of_stock_items = generate_bill(cart, inventory_file, output_file)

if out_of_stock_items:
    print("Out of stock items:", out_of_stock_items)
else:
    print(f"Total Price: ${total_price:.2f}")