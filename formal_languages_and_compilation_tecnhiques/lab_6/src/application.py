import sys
from finite_automata import FiniteAutomata


class Application(object):
    def __init__(self):
        self.__initialize_main_menu()
        self.__initialize_finite_automata()

    def run(self):
        while True:
            self.__print_menu()
            try:
                self.__handle_user_command()
            except (AssertionError, ValueError):
                print("Invalid option! Please choose a number between 0 and 6.")

    def __initialize_main_menu(self):
        self.__main_menu = [
            "Quit the application.",
            "Display the initial state.",
            "Display the set of states.",
            "Display the alphabet.",
            "Display the set of transitions",
            "Display the set of final states.",
            "In case of DFA, verify if a sequence is accepted by the DFA."
        ]

    def __initialize_finite_automata(self):
        self.__finite_automata = FiniteAutomata()
        self.__finite_automata.load()

    def __print_menu(self):
        print("========= MENU =========")
        for index, option in enumerate(self.__main_menu):
            print(f"{index}. {option}")
        print("========================")

    def __handle_user_command(self):
        command = self.__read_command()

        if command == 0:
            sys.exit()
        elif command == 1:
            print(self.__finite_automata.initial_state)
        elif command == 2:
            print(self.__finite_automata.states)
        elif command == 3:
            print(self.__finite_automata.alphabet)
        elif command == 4:
            print(self.__finite_automata.transitions_to_string())
        elif command == 5:
            print(self.__finite_automata.final_states)
        elif command == 6:
            print(self.__perform_sequence_acceptance_check())

    def __perform_sequence_acceptance_check(self) -> str:
        if not self.__finite_automata.is_deterministic():
            return "The specified FA is NOT a DFA."

        sequence = input("Enter sequence: ")
        if self.__finite_automata.is_sequence_accepted(sequence):
            return "Sequence accepted."
        return "Sequence NOT accepted."

    def __read_command(self) -> int:
        command = int(input("Enter option: "))
        assert 0 <= command <= len(self.__main_menu)
        return command

