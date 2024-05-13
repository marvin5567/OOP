"""
Inventory Management System

Concepts: Polymorphism, Abstract Classes, File Handling
Description: Create a system to manage an inventory for a small business or personal collection (like books, electronics, etc.). Use classes to represent different types of inventory items, and implement polymorphic behavior to handle various methods of item categorization or valuation. You could use file handling for saving and loading inventory data.
Outcome: A functional inventory system that can be scaled or customized according to user needs, perfect for small business owners or collectors.
"""

import player
import item

user = player.Player("meow", 100, 10, 10, False)

steak = item.Item(0, "Steak", "its a steak", "food")

print(steak)