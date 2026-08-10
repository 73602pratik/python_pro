inventory = [
    {
        "product_name": "Laptop",
        "product_id": "PL0001",
        "price": 1200.00,
        "stock_quantity": 10,
        "category": "Electronics"
    },
    {
        "product_name": "Smartphone",
        "product_id": "PL0002",
        "price": 800.00,
        "stock_quantity": 20,
        "category": "Electronics"
    },
    {
        "product_name": "Headphones",
        "product_id": "PL0003",
        "price": 150.00,
        "stock_quantity": 15,
        "category": "Electronics"
    }
]

for item in inventory:
    print("Product Name:", item["product_name"])
    print("Product ID:", item["product_id"])
    print("Product Price:", item["price"])
    print("Stock Quantity:", item["stock_quantity"])
    print("Category:", item["category"])
    print()

print(type(inventory[0]["product_name"]))  # Output: <class 'str'>
print((type(inventory[0]["price"])))  # Output: <class 'float'>
print(type(inventory[0]["stock_quantity"]))  # Output: <class 'int'>

print(id(inventory))
inventory_backup = inventory
print(id(inventory_backup))  # Output: Same as id(inventory)
print(id(inventory))

new_item = {
    "product_name": "Tablet",
    "product_id": "PL0004",
    "price": 500.00,
    "stock_quantity": 5,
    "category": "Electronics"
}
inventory_backup.append(new_item)
print(inventory_backup)  # Output: Same as inventory with the new item added
print(inventory)  # Output: Same as inventory with the new item added

print(inventory is inventory_backup)  # Output: True
print(inventory == inventory_backup)  # Output: True