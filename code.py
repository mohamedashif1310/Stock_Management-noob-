class StockManager:
    def __init__(self):
        self.stock = 10
        self.amount = 1000
        self.value = 200

    def display_options(self):
        print("ENTER OPTION :-")
        print("-" * 50)
        print("1. SELL")
        print("2. PURCHASE")
        print("*" * 50)

    def sell_stock(self):
        print("YOU ARE NOW SELLING....")
        quantity = int(input("ENTER QUANTITY OF STOCK: "))
        if quantity <= self.stock:
            self.stock -= quantity
            payable_amount = quantity * self.value
            self.amount += payable_amount
            print(f'REMAINING STOCK: {self.stock}')
            print(f'PAYABLE AMOUNT $$: {payable_amount}')
            print(f'BALANCE AMOUNT: {self.amount}')
        else:
            print("INSUFFICIENT STOCK")

    def purchase_stock(self):
        print("PURCHASING IS IN PROGRESS....")
        quantity = int(input("ENTER QUANTITY OF STOCK: "))
        total_amount = quantity * self.value
        if total_amount <= self.amount:
            self.stock += quantity
            self.amount -= total_amount
            print(f'REMAINING STOCK: {self.stock}')
            print(f'AMOUNT $$: {total_amount}')
        else:
            print("INSUFFICIENT FUNDS")

    def process_option(self, option):
        if option == 1:
            self.sell_stock()
        elif option == 2:
            self.purchase_stock()
        else:
            print("INVALID OPTION")


manager = StockManager()
manager.display_options()
option = int(input("Enter the Option: "))
manager.process_option(option)
