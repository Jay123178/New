lorry_capacity = 1000  
lorry_load = 0
deliveries = []
balance = 0

def display_menu():
 print("\nLorry Game")
 print("1. Deliver Goods")
 print("2. Check Lorry Load")
 print("3. View Deliveries")
 print("4. Check Balance")
 print("5. Quit")

def deliver_goods():
 global lorry_load, balance
 goods_weight = int(input("Enter weight of goods to deliver (kg): "))
 goods_value = int(input("Enter value of goods: "))
 if lorry_load + goods_weight <= lorry_capacity:
  lorry_load += goods_weight
  deliveries.append({"weight": goods_weight, "value": goods_value})
  balance += goods_value
  print("Goods delivered successfully!")
 else:
  print("Lorry is fully loaded!")

def check_lorry_load():
 print(f"Lorry Load: {lorry_load}/{lorry_capacity} kg")

def view_deliveries():
 print("Deliveries:")
 for delivery in deliveries:
  print(f"Weight: {delivery['weight']} kg, Value: {delivery['value']}")

def check_balance():
 print(f"Balance: {balance}")

while True:
 display_menu()
 choice = input("Enter your choice: ")
 if choice == "1":
  deliver_goods()
 elif choice == "2":
  check_lorry_load()
 elif choice == "3":
  view_deliveries()
 elif choice == "4":
  check_balance()
 elif choice == "5":
  break
 else:
  print("Invalid choice!")