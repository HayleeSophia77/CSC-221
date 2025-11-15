# Autograder Main Menu
# 10/11/2025
# M4GroupPro
# Haylee

# Ex: from grading_system import grade_module1, grade_module3, grade_module4, grade_module5

def main():
    choice = ""

    while choice != "5":
        print("\n------------- MENU ----------------")
        print("1. Module 1 (Basic input and output)")
        print("2. Module 3 (Loops)")
        print("3. Module 4 (Functions)")
        print("4. Module 5 (Reading Files)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\n[Module 1 Selected]")
            # TODO: Module 1 function here
            # Ex: grade_module1()
            pass

        elif choice == "2":
            print("\n[Module 3 Selected]")
            # TODO: Module 3 function here
            # Ex: grade_module3()
            pass

        elif choice == "3":
            print("\n[Module 4 Selected]")
            # TODO: Module 4 function here
            # Ex: grade_module4()
            pass

        elif choice == "4":
            print("\n[Module 5 Selected]")
            # TODO: Module 5 function here
            # Ex: grade_module5()
            pass

        elif choice == "5":
            print("\nExiting program. Goodbye!")

        else:
            print("\nInvalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()