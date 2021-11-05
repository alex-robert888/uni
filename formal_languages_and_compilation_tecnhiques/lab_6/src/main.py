def print_menu():
    print("========= MENU =========")
    print("1. Set of states.")
    print("2. Alphabet.")
    print("3. Set of transitions.")
    print("4. Set of final states.")
    print("5. For a DFA, verify if a sequence is accepted by the FA")
    print("========================")


if __name__ == '__main__':

    while True:
        print_menu()

        option = 0
        try:
            option = int(input("Enter option: "))
            assert 1 <= option <= 5
        except:
            print("Invalid option!")

        if option == 1:
            pass
        elif option == 2:
            pass
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass


