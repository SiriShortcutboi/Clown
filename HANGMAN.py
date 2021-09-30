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

##print(len(HANGMAN)


WORDS = ("PRINT","SNAKE","PYTHON","INPUT","SYSTEM","DEVELOPMENT","LIFE","CYCLE","REQUIREMENT","ANALYSIS","DESIGN","EVOLUTION","TESTING","IMPLEMENTATION","IDLE","BETTER","THAN","LESS","THAN","PROGRAMMER","INVALID","SYNTAX","STRING","TUPPLE",)
#pick word to be guesssed

x = random.randint(0,(len(WORDS)-1))
word = WORDS[x]

so_far="-"*len(word)

print(so_far)

