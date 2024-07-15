
player_name = input("Enter your name: ")
player_location = "village"

inventory = []

def display_location():
 print(f"You are in the {player_location}.")
 if player_location == "village":
  print("You see a path leading to a cave.")
 elif player_location == "cave":
  print("You see a chest in the corner.")

def move_location(direction):
 global player_location
 if direction == "north" and player_location == "village":
  player_location = "cave"
  print( player_location )
 elif direction == "south" and player_location == "cave":
  player_location = "village"
  print( player_location )
 else:
  print("You can't go that way!")

def collect_item(item):
 inventory.append(item)
 print(f"You collected a {item}!")

def solve_puzzle():
 if "key" in inventory:
  print("You unlocked the chest!")
 else:
  print("You need a key to unlock the chest!")

while True:
 print("\nAdventure Game")
 print("1. Display Location")
 print("2. Move")
 print("3. Collect Item")
 print("4. Solve Puzzle")
 print("5. Quit")
 choice = input("Enter your choice: ")

 if choice == "1":
  display_location()
 elif choice == "2":
  direction = input("Enter direction (north/south): ")
  move_location(direction)
 elif choice == "3":
  item = input("Enter item to collect: ")
  collect_item(item)
 elif choice == "4":
  solve_puzzle()
 elif choice == "5":
  break
 else:
  print("Invalid choice!")