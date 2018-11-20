#Hayden Whitney
#11/18
#A trivia word search game


def menu():
  welcome()
  print("[0] Tutorial")
  print("[1] Play")
  print("[2] Score")
  print("[3] Credits")
  choice = input("\nEnter the [#] of your choice: ")
  if choice == "0":
    tutorial()
  elif choice == "1":
    game()
  elif choice == "2":
    score()
  elif choice == "3":
    credits()
  else:
    print("Please enter a valid choice.")
    menu()

def credits():
  print("\nThis game was made possible by Matthew Walker, Hayden Whitney, and users like you. Thank you.")
  return_to_menu = input("\nPress the enter key to return to menu.\n")
  menu()



menu()
