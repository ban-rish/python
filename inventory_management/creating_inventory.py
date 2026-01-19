# we will create a file with inventory as follows - 
# 1. Serial Number
# 2. product Name
# 3. Price 
# 4. Quantity

# fd = open(r"C:\Users\bansa\Personal\github\python\inventory_management\inventory.txt","w")
# fd.close()

fc = open(r"C:\Users\bansa\Personal\github\python\inventory_management\inventory.txt","r")
txt = fc.read()
fc.close()
print(txt)
txt.split("\n")
print(txt)

# Generating Bill and updating Inventory
products = txt.split("\n")
ui_input_id = input("Enter Product ID: ")
for product in products:
    if product.split(',')[0] == ui_input_id:
        product_details = product.split(',')
        print(product_details)
        ui_input_quantity = int(input("Enter Quantity : "))
        money = ui_input_quantity*int(product_details[2])
        print("Please Pay ",money)
        product_details[3] = str(int(product_details[3])-ui_input_quantity)
        print(product_details) 
print(products)