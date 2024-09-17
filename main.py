from colored import Fore, Back, Style

print(f"{Fore.yellow}{Back.red}Welcome to the Carpark Application!!!{Style.reset}\n")

def create_menu():

    print("Enter 1 to add a parking slot.")
    print("Enter 2 to delete a parking slot.")
    print("Enter 3 to list all the parking slots.")
    print("Enter 4 to park car.")
    print("Enter 5 to find a parking slot.")
    print("Enter 6 to remove a car from the carpark")
    print("Enter 7 to exit")

    choice = input("Enter your choice: ")
    return choice

user_choice = ""
while user_choice != "7":
    user_choice = create_menu()

    if user_choice =="1":
        print("Add slot")
    elif user_choice =="2":
        print("Delete slot")
    elif user_choice =="3":
        print("List slots")
    elif user_choice =="4":
        print("Park car")
    elif user_choice =="5":
        print("Find car")
    elif user_choice =="6":
        print("Remove Car")
    elif user_choice =="7":
        print("Exiting")
    else:
        print("Invalid Input")

print("Thank you for using the carpark application")
