class VendingMachine:
    def __init__(self):
        self.soda = 8
        self.coffee = 7
        self.water = 11

    def purchase(self, drink_type, amount):
        """Purchase a specified amount of a selected drink type."""
        if drink_type == 'soda' and self.soda >= amount:
            self.soda -= amount
            print(f'You purchased {amount} Soda(s).')
        elif drink_type == 'water' and self.water >= amount:
            self.water -= amount
            print(f'You purchased {amount} Water bottle(s).')
        elif drink_type == 'coffee' and self.coffee >= amount:
            self.coffee -= amount
            print(f'You purchased {amount} Coffee(s).')
        else:
            print(f'Sorry, not enough {drink_type} available or invalid drink.')

    def restock(self, drink_type, amount):
        """Restock a specified drink type with the given amount."""
        if drink_type == 'soda':
            self.soda += amount
            print(f'{amount} Soda(s) have been added.')
        elif drink_type == 'water':
            self.water += amount
            print(f'{amount} Water bottle(s) have been added.')
        elif drink_type == 'coffee':
            self.coffee += amount
            print(f'{amount} Coffee(s) have been added.')
        else:
            print(f'Invalid drink type: {drink_type}')

    def retrieve_inventory(self):
        """Print the current inventory of each drink type."""
        print("Current Inventory:")
        print(f'Soda: {self.soda}')
        print(f'Water: {self.water}')
        print(f'Coffee: {self.coffee}')

# Main program to interact with the Vending Machine
def main():
    vending_machine = VendingMachine()
    
    print("Welcome to the Vending Machine!")
    print("Commands:")
    print("- purchase <drink_type> <amount> (e.g., 'purchase soda 2')")
    print("- restock <drink_type> <amount> (e.g., 'restock water 5')")
    print("- inventory - Show current inventory")
    print("- quit or q - Exit the program")

    while True:
        # Read user command
        user_input = input("\nEnter a command: ").strip().lower()
        if user_input in ['quit', 'q']:
            print("Exiting the vending machine. Goodbye!")
            break

        # Split user input into command and arguments
        parts = user_input.split()
        if len(parts) == 0:
            print("Invalid command. Please try again.")
            continue

        command = parts[0]

        # Handle different commands
        if command == "purchase" and len(parts) == 3:
            drink_type = parts[1]
            try:
                amount = int(parts[2])
                vending_machine.purchase(drink_type, amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif command == "restock" and len(parts) == 3:
            drink_type = parts[1]
            try:
                amount = int(parts[2])
                vending_machine.restock(drink_type, amount)
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        elif command == "inventory":
            vending_machine.retrieve_inventory()
        else:
            print("Unknown command. Please try again.")

# Run the main program
main()

