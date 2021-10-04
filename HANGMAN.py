##Holden Anderson
##Hangman
##9/21

##imports
import random

##create art

HANGMAN = (


"""
 ------
 |    |
 |
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |
 |
 |
 |
 |
 |
----------
""",
"""
 ------
 |    |
 |    O
 |   -+-
 | 
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-/
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\
 |   
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\
 |    |
 |   
 |   
 |   
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\
 |    |
 |    |
 |   | 
 |   | 
 |   
----------
""",
"""
 ------
 |    |
 |    O
 |  /-+-\
 |    |
 |    |
 |   | |
 |   | |
 |  
----------
""")
WORDS = ("PRINT","SNAKE","PYTHON","INPUT","SYSTEM","DEVELOPMENT","LIFE","CYCLE","REQUIREMENT","ANALYSIS","DESIGN","EVOLUTION","TESTING","IMPLEMENTATION","IDLE","BETTER","LESS","THAN","PROGRAMMER","INVALID","SYNTAX","STRING","TUPPLE",)
#pick word to be guesssed


word = random.choice(WORDS)
x = random.randint(0,(len(WORDS)-1))
word = WORDS[x]

so_far="-"*len(word)

MAX_WRONG = len(HANGMAN)-1

print(MAX_WRONG)
wrong = 0
used = []
#welcome palyer to the game
print("Welcome to Hangman. Good luck!")

#start Game Loop

while so_far != word and wrong < MAX_WRONG:

    print(HANGMAN[wrong])
    print("Guessed Letters",used)
    print("Guessed Word so far:",so_far)
    #get users guess
    guess = input("Guess your next letter")
    #convert guess to all uppercase
    guess = guess.upper()

    #check to see if letter has been used
    print (guess.isalpha())
    while guess in used or len(guess)>1 or guess.isnumeric() or not guess.isalpha():
        if len(guess)>1:
           print ("Try just one letter") 
        elif guess.isnumeric():
           print("I'm looking for a letter not a number")
        elif not guess.isalpha():
            print("I'm looking for a letter not a special character")
        else:
            print("You've already guessed the letter",guess)
            guess = input("Guess a Letter")
            guess = guess.upper()


    used.append(guess)
    if guess in word :
        print("\nYes!",guess,"is in the word!")

#create a variable to hold the temporary word
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]

        so_far = new
    else:
        print("\nSorry,",guess,"isn't in the word.")
        wrong+=1

if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    input("game over you have been hung")
else:
    print(HANGMAN[wrong])
    print("You guessed it!")

print("\nThe word was", word)
input("Press the enter key to exit.")
