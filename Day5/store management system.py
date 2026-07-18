categories=3
products=4
inventory=[]
for i in range(categories):
    print(f"\ncategory {i+1}")
    category=[]
    for j in range(products):  
        qty=int(input(f"Enter the quantity of product {j+1}: "))
        category.append(qty)
    inventory.append(category)
print("\nWarehouse inventory:")

for i in range(categories):
    print(f"category{i+1}")
    for j in range(products):
        print(f"Product {j+1}= {inventory[i][j]}")