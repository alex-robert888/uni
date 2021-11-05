class FiniteAutomata(object):
    def __init__(self, file_path):
        self.file_path = file_path

    def load_sizes(self, f):
        line = f.readline().split()
        self.


    def load_states(self, f):
        pass

    def load_initial_state(self, f):
        pass

    def load_final_states(self, f):
        pass

    def load(self):
        f = open("finite_automata_1.txt", "r")
        self.load_sizes(f)
        self.load_states(f)
        self.load_initial_state(f)
        self.load_final_states(f)




