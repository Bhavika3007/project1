# Function to add an item to the menu
def add_item(menu, item):
    menu.append(item)  # Add item to the menu
    return menu

# Function to remove an item from the menu
def remove_item(menu, item):
    if item in menu:
        menu.remove(item)  # Remove item if it exists in the menu
    else:
        print(f"Error: '{item}' is not available on the menu.")
    return menu
def check_item(menu, item):
    if item in menu:
        return f"{item} is available"
    else:
        return f"{item} is not available"

initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]

add_item_input = "Tacos"
remove_item_input = "Salad"
check_item_input = "Pizza"

updated_menu = add_item(initial_menu, add_item_input)  
updated_menu = remove_item(updated_menu, remove_item_input)  

availability = check_item(updated_menu, check_item_input)

print(f"Updated menu: {updated_menu}")
print(f"Availability: {availability}")
