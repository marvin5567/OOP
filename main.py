"""
Inventory Management System

Concepts: Polymorphism, Abstract Classes, File Handling
Description: Create a system to manage an inventory for a small business or personal collection (like books, electronics, etc.). Use classes to represent different types of inventory items, and implement polymorphic behavior to handle various methods of item categorization or valuation. You could use file handling for saving and loading inventory data.
Outcome: A functional inventory system that can be scaled or customized according to user needs, perfect for small business owners or collectors.
"""

import player
import item

user = player.Player("joe", 100, 100, 20, 20, 10, 10, False)

sushi = item.FOOD(0, "sushi", "its sushi", "food", 10, 10)
spoiledSushi = item.FOOD(0, "spoiled sushi", "its sushi", "food", 10, -10)
print(sushi.id)
>>>>>>>>> Temporary merge branch 2

while user.isDead == False:
    print("What would you like to do?\n--------------------------")
    print("\n> Eat food!\n>Eat totally not spoiled food\n>Check Health")
    choice = input("")

    if choice == "ef":
        user.healthChange(sushi.healthGain)
    
    if choice == "efn":
        user.healthChange(spoiledSushi.healthGain)
    
    if choice == "ch":
        print(f"HP: {user.health}/{user.maxHealth}")
