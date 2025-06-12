from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")
# Puzzle 0
knowledge0 = And(
    # A says "I am both a knight and a knave."
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Implication(AKnight, And(AKnight, AKnave)),
    Implication(AKnave, Not(And(AKnight, AKnave)))
)
# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),

    Implication(AKnight, And(AKnave, BKnave)),
    Implication(AKnave, Not(And(AKnave, BKnave)))
)



# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
  
    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),


    Implication(AKnight, Or(
        And(AKnight, BKnight),  
        And(AKnave, BKnave)    
    )),
    Implication(AKnave, Not(Or(
        And(AKnight, BKnight),  
        And(AKnave, BKnave)
    ))),


    Implication(BKnight, Or(
        And(AKnight, BKnave),  
        And(AKnave, BKnight)   
    )),
    Implication(BKnave, Not(Or(
        And(AKnight, BKnave),   
        And(AKnave, BKnight)
    )))
)


# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
A_said_knight = Symbol("A said 'I am a Knight'")
A_said_knave = Symbol("A said 'I am a Knave'")

knowledge3 = And(

    Or(AKnight, AKnave),
    Or(BKnight, BKnave),
    Or(CKnight, CKnave),
    Not(And(AKnight, AKnave)),
    Not(And(BKnight, BKnave)),
    Not(And(CKnight, CKnave)),


    Or(A_said_knight, A_said_knave),
    Not(And(A_said_knight, A_said_knave)),

    Implication(A_said_knight, Biconditional(AKnight, AKnight)),
    Implication(A_said_knave, Biconditional(AKnight, Not(AKnight))),

    # B's statements about A and C
    Implication(BKnight, And(A_said_knave, CKnave)),
    Implication(BKnave, And(Not(A_said_knave), Not(CKnave))),

    # C's statement about A
    Implication(CKnight, AKnight),
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
