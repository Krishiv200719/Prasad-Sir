class Restaurant:
    def __init__(self):
        self.menu = {
            "Pizza": 250,
            "Burger": 120,
            "Pasta": 180,
            "Fries": 90,
            "Coffee": 80
        }

    def show_menu(self):
        print("---- MENU ----")
        for item, price in self.menu.items():
            print(f"{item}: Rs.{price}")

    def calculate_bill(self, order_list):
        total = 0
        print("\n---- BILL ----")
        for item in order_list:
            if item in self.menu:
                price = self.menu[item]
                total += price
                print(f"{item} - Rs.{price}")
            else:
                print(f"{item} - Not available")
        print("----------------")
        print(f"Total Amount: Rs.{total}")

restaurant = Restaurant()
restaurant.show_menu()

order = ["Pizza", "Coffee", "Ice Cream"] 
restaurant.calculate_bill(order)
