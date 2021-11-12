from collections import defaultdict


class FiniteAutomata:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.initial_state = None
        self.final_states = set()
        self.transitions = defaultdict(lambda: defaultdict(list))

    def load(self):
        f = open("../resources/dfa-starting-with-0.in", "r")
        self.__load_states(f)
        self.__load_alphabet(f)
        self.__load_initial_state(f)
        self.__load_final_states(f)
        self.__load_transitions(f)

    def transitions_to_string(self) -> str:
        output = ""
        for state_name, state_dict in self.transitions.items():
            for input_value, list_of_destinations in state_dict.items():
                list_of_destinations_to_string = ' '.join([str(destination) for destination in list_of_destinations])
                output += f"{state_name} ({input_value})-> {list_of_destinations_to_string}\n"
        return output

    def is_deterministic(self) -> bool:
        for state_name, state_dict in self.transitions.items():
            input_values = state_dict.keys()
            if len(input_values) != len(self.alphabet) or len(input_values) != len(set(input_values)):
                return False

            for input_value, list_of_destinations in state_dict.items():
                if len(list_of_destinations) != 1:
                    return False
        return True

    def is_sequence_accepted(self, sequence: str) -> bool:
        state = self.initial_state
        for input_value in sequence:
            if input_value not in self.alphabet:
                return False
            state = self.transitions[state][input_value][0]
        return state in self.final_states

    def __load_states(self, f):
        self.states = f.readline().split()

    def __load_alphabet(self, f):
        self.alphabet = f.readline().split()

    def __load_initial_state(self, f):
        self.initial_state = f.readline().split()[0]
        if self.initial_state not in self.states:
            raise Exception('Initial state is not a valid state!')

    def __load_final_states(self, f):
        self.final_states = f.readline().split()
        for state in self.final_states:
            if state not in self.states:
                raise Exception(f"Final state {state} is not a valid state!")

    def __load_transitions(self, f):
        while transition := f.readline().split():
            source, destination, input_value = transition[0], transition[1], transition[2]
            if source not in self.states:
                raise Exception(f"Source state {source} is not a valid state!")
            if destination not in self.states:
                raise Exception(f"Source state {destination} is not a valid state!")
            if input_value not in self.alphabet:
                raise Exception(f"Source state {input_value} is not a valid input!")

            self.transitions[source][input_value].append(destination)
