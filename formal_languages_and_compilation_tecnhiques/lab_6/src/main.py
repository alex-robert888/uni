from finite_automata import FiniteAutomata

finite_automata = FiniteAutomata()


def print_menu():
    print("========= MENU =========")
    print("0. Initial state.")
    print("1. Set of states.")
    print("2. Alphabet.")
    print("3. Set of transitions.")
    print("4. Set of final states.")
    print("5. For a DFA, verify if a sequence is accepted by the FA")
    print("========================")


def is_sequence_accepted(sequence):
    pass


if __name__ == '__main__':
    finite_automata.load()

    while True:
        print_menu()

        option = 0
        try:
            option = int(input("Enter option: "))
            assert 0 <= option <= 5
        except:
            print("Invalid option!")

        if option == 0:
            print(finite_automata.initial_state)
        elif option == 1:
            print(finite_automata.states)
        elif option == 2:
            print(finite_automata.alphabet)
        elif option == 3:
            print(finite_automata.transitions)
        elif option == 4:
            print(finite_automata.final_states)
        elif option == 5:
            sequence = input("Enter sequence")
            if is_sequence_accepted(sequence):
                print("Sequence NOT accepted")
            else:
                print("Sequence accepted.")



