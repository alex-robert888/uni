class Transition:
    def __init__(self, source, destination, input):
        self.source = source
        self.destination = destination
        self.input = input

    def __str__(self):
        return f'source: {self.source} | destination: {self.destination} | input: {self.input}'


class FiniteAutomata:
    def __init__(self):
        self.states = list()
        self.alphabet = list()
        self.initial_state = list()
        self.final_states = list()
        self.transitions = dict()

    def load(self):
        f = open("./resources/FA.in", "r")
        self.load_states(f)
        self.load_alphabet(f)
        self.load_initial_state(f)
        self.load_final_states(f)
        self.load_transitions(f)

    def load_states(self, f):
        self.states = f.readline().split()

    def load_alphabet(self, f):
        self.alphabet = f.readline().split()

    def load_initial_state(self, f):
        self.initial_state = f.readline().split()[0]

    def load_final_states(self, f):
        self.final_states = f.readline().split()

    def load_transitions(self, f):
        while transition := f.readline().split():
            source = transition[0]
            destination = transition[1]
            input = transition[2]

            if input not in self.transitions:
                self.transitions[input] = [(source, destination)]
            else:
                self.transitions[input].append((source, destination))
