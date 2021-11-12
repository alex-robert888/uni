# Laboratory 4

## Statement

Write a program that:

1. Reads the elements of a FA (from file)

2. Displays the elements of a finite automata, using a menu: the set of states, the alphabet, all the transitions, the set of final states.

3. For a DFA, verify if a sequence is accepted by the FA.

## Finite Automata Model

I created a class for the Finite Automata, with the following state:
* states: set of strings representing the states of the FA
* alphabet: set of strings representing the alphabet (set of inputs) of the FA
* initial_state: a string representing the initial state of the FA (which should be present in the set of states)
* final_states: a set of strings representing the final sates of the FA (which should be present in the set of states)
* transitions: a dictionary represing the set of transactions. The dictionary maps the source states to their destination states, together with input leading to that destination state. More precisely, we have a dictionary of dictionaries, in which the inner dictionary maps the inputs to the list of destination states and the wrapper dictionary maps the source states to that inner dictionary (holding the inputs and destination states).

{
       A: {
              0: [A],
              1: [B, C]
       },
       B: {
              0: [C],
              1: [A]
       },
       C: {
              0: [C],
              1: [A, C]
       }
}

## Input File Specified in EBNF

letter ::= "A" | "B" | "C" | "D" | "E" | "F" | "G"
       | "H" | "I" | "J" | "K" | "L" | "M" | "N"
       | "O" | "P" | "Q" | "R" | "S" | "T" | "U"
       | "V" | "W" | "X" | "Y" | "Z" | "a" | "b"
       | "c" | "d" | "e" | "f" | "g" | "h" | "i"
       | "j" | "k" | "l" | "m" | "n" | "o" | "p"
       | "q" | "r" | "s" | "t" | "u" | "v" | "w"
       | "x" | "y" | "z" ;
       
digit ::= "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" ;

symbol ::= "[" | "]" | "{" | "}" | "(" | ")" | "<" | ">"
       | "'" | '"' | "=" | "|" | "." | "," | ";" ;
       
character ::= letter | digit | symbol | "_" ;

identifier ::= {character};

state ::= identifier;

states ::= {state};

input_value ::= character;

alphabet ::= {input_value};

initial_state ::= identifier;

final_states ::= {identifier};

transition ::= state, state, input_value;

transitions ::= {"\n", transition};

input_file ::= states, "\n", alphabet, "\n", initial_state, "\n", final_states, transitions;
