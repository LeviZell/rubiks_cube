import numpy as np
import tkinter as tk

from rubiks_print_2x2 import *
from rubiks_controls_2x2 import *
from rubiks_cube_2x2 import *

def main():
  """
  Function for playing with a 2x2 Rubik's Cube  
      
  """
    
  # build cube
  rubiks_cube=RubiksCube2x2()  
  
  # start tkinter to read keyboard inputs
  keboard=KeyControls2x2()
  
  # play until quite or completed
  # while in_game=True and not is_complete: 
  
if __name__ == '__main__':
  main()
  