# Finite Automata

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
input_value ::= identifier;
alphabet ::= {input_value};
initial_state ::= identifier;
final_states ::= {identifier};
transition ::= state, state, input_value;
transitions ::= {"\n", transition};

input_file ::= states, "\n", alphabet, "\n", initial_state, "\n", final_states, transitions;
