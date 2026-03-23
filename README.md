digitalpos
Project: "The Digital POS System."
Goal: Create a professional-grade POS System that handles a full dining experience.
Pseudocode Breakdown:
Phase 1: Setup
-Create a "Menu" list with names and prices.
-Prepare an empty "Cart" (like a shopping basket) to store the food and how many of each are picked.
-Ask for the Table Number so we know where the food is going.
Phase 2: The Ordering Loop (The "While" Loop)
-Ask the user: "What would you like to order?"
-If they type food: Look it up in the menu. Add it to the cart. If they already have one, change the number from 1 to 2.
-If they type "Remove": Ask which item to take back. Subtract 1 from their count. If they have 0 left, take that item off their list completely.
-If they type "Done": Stop asking for food and move to the bill.
Phase 3: The Tip & The Split
-Show the user a few "Suggested Tips" so they don't have to do the math in their head.
-Ask for a tip. If they use a %, calculate that portion of the bill. If they use a $, just add that amount.
-Ask how many people are sitting at the table to calculate the "per person" cost.
Phase 4: The Final Receipt
-Do the final math: Food Total + 9.5% Tax + Tip = Grand Total.
-Print a beautiful receipt showing the Table Number at the top.
-List every item bought, how many were ordered, and the total for that specific item (e.g., 2x Steak: $90.00).
-Show the final price each person owes.
