from collections import defaultdict


class FiniteAutomata:
    def __init__(self):
        self.states = set()
        self.alphabet = set()
        self.initial_state = set()
        self.final_states = set()
        self.transitions = defaultdict(list)

    def is_sequence_accepted(self, sequence: str) -> bool:
        return True

    def load(self):
        f = open("../resources/FA.in", "r")
        self.__load_states(f)
        self.__load_alphabet(f)
        self.__load_initial_state(f)
        self.__load_final_states(f)
        self.__load_transitions(f)

    def __load_states(self, f):
        self.states = f.readline().split()

    def __load_alphabet(self, f):
        self.alphabet = f.readline().split()

    def __load_initial_state(self, f):
        self.initial_state = f.readline().split()[0]

    def __load_final_states(self, f):
        self.final_states = f.readline().split()

    def __load_transitions(self, f):
        while transition := f.readline().split():
            source, destination, input_value = transition[0], transition[1], transition[2]
            self.transitions[input_value].append((source, destination))
