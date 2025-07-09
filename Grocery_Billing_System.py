import random

def roll_dice():
    while True:
        try:
            dice = int(input("How many dice to roll? (1-6): "))
            if dice < 1 or dice > 6:
                print("Enter a number between 1 and 6.")
                continue
        except ValueError:
            print("Invalid input.")
            continue

        print("Rolling...")
        for i in range(dice):
            print(f"Dice {i+1}: {random.randint(1, 6)}")

        again = input("Roll again? (y/n): ").lower()
        if again != 'y':
            print("Goodbye.")
            break

roll_dice()
class Store:
    def __init__(self):
        self.items = []

    def add_item(self):
        name = input("Item name: ")
        try:
            qty = float(input("Quantity: "))
            price = float(input("Price per unit: "))
            if qty <= 0 or price <= 0:
                print("Invalid quantity or price.")
                return
            self.items.append((name, qty, price))
        except ValueError:
            print("Enter numbers only.")

    def print_bill(self):
        if not self.items:
            print("No items added.")
            return
        total = 0
        print("\n--- Bill ---")
        print("{:<15}{:<10}{:<10}{:<10}".format("Item", "Qty", "Price", "Total"))
        for name, qty, price in self.items:
            item_total = qty * price
            total += item_total
            print("{:<15}{:<10}{:<10}{:<10.2f}".format(name, qty, price, item_total))
        print("-" * 45)
        print(f"{'Total Amount:':<35} ₹{total:.2f}")
        print("-" * 45)

    def run(self):
        while True:
            print("\n1. Add Item")
            print("2. Print Bill")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.print_bill()
            elif choice == "3":
                print("Thank you.")
                break
            else:
                print("Invalid choice.")

store = Store()
store.run()
