"""
Inventory Management System

Concepts: Polymorphism, Abstract Classes, File Handling
Description: Create a system to manage an inventory for a small business or personal collection (like books, electronics, etc.). Use classes to represent different types of inventory items, and implement polymorphic behavior to handle various methods of item categorization or valuation. You could use file handling for saving and loading inventory data.
Outcome: A functional inventory system that can be scaled or customized according to user needs, perfect for small business owners or collectors.
"""

import player
import item
import entity

# player
user = player.Player("joe", 100, 100, 20, 20, -10, 10, False)

# foods
sushi = item.FOOD(0, "sushi", "its sushi", "food", 10, 10)
spoiledSushi = item.FOOD(0, "spoiled sushi", "its sushi", "food", 10, -10)

# entities
jerry = entity.Enemy(50, "Jerry", 50, 10, "Enemy", "hostile")
mostafa = entity.NPC(50, "Mostafa", 50, 10, "npc", "peaceful")
duck = entity.Animal("duck", 100, 100, 99, "animal", "agressive")

while user.health > 0:
    print("What would you like to do?\n--------------------------")
    print("\n>Eat food!\n>Eat totally not spoiled food\n>Check Health")
    choice = input("")

    if choice == "ef":
        user.healthChange(sushi.healthGain)
    
    if choice == "efn":
        user.healthChange(spoiledSushi.healthGain)
    
    if choice == "ch":
        print(f"\nHP: {user.health}/{user.maxHealth}")

    if user.health <= 0:
        print("you died ;(")
        break

    print("\nnow lets attack a bitch\n-----------------------")
    print(">Jerry\n>Mostafa\n>Duck")
    choiceTwo = input("")

    if choiceTwo == "j":
        jerry.healthChange(user.dmg)
        print(jerry.healthDisplay())

    if choiceTwo == "m":
        mostafa.healthChange(user.dmg)
        print(mostafa.healthDisplay())

    if choiceTwo == "d":
        duck.healthChange(user.dmg)
        print(duck.healthDisplay())
        print("meow")
    