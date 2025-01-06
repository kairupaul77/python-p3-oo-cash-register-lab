class CashRegister:
    def __init__(self):
        self.total = 0  # To track the total price
        self.items = []  # To track the items added to the register
        self.last_transaction = 0  # To keep track of the last transaction

    def add_item(self, price, quantity=1):
        """Add an item to the register."""
        self.total += price * quantity
        self.items.append((price, quantity))  # Store price and quantity of the item
        self.last_transaction = price * quantity  # Keep track of the last transaction

    def apply_discount(self, discount):
        """Apply a discount (percentage) to the total."""
        if discount > 0:
            discount_amount = self.total * (discount / 100)
            self.total -= discount_amount
            return f"After the discount, the total comes to ${self.total:.2f}"
        return "There is no discount to apply."

    def void_last_transaction(self):
        """Remove the last transaction from the total."""
        self.total -= self.last_transaction
        # Ensure that last_transaction is reset after voiding
        self.last_transaction = 0

    def get_total(self):
        """Return the current total."""
        return self.total
