#####################
# Welcome to Cursor #
#####################

'''
Step 1: Try generating with Cmd+K or Ctrl+K on a new line. Ask for CLI-based game of TicTacToe.

Step 2: Hit Cmd+L or Ctrl+L and ask the chat what the code does. 
   - Then, try running the code

Step 3: Try highlighting all the code with your mouse, then hit Cmd+k or Ctrl+K. 
   - Instruct it to change the game in some way (e.g. add colors, add a start screen, make it 4x4 instead of 3x3)

Step 4: To try out cursor on your own projects, go to the file menu (top left) and open a folder.
'''

import gensim.downloader

def add(a: int, b: int) -> int:
    """
    Returns the sum of two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of a and b.
    """
    return a + b

def subtract(a: int, b: int) -> int:
    """
    Returns the difference between two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The difference between a and b.
    """
    return a - b

print(add(5, 2.0))
print(subtract(5, 2.0))

model = gensim.downloader.load("glove-wiki-gigaword-50")
model["tower"]