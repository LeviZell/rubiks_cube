""" 
Keyboard Controls for Rubik's Cube game - RubiksCube2x2.py

"""

import numpy as np
import tkinter as tk
import time

from rubiks_print_2x2 import *
from rubiks_cube_2x2 import * 


class KeyControls2x2(tk.Frame):
  
  game_cube = RubiksCube2x2()

  def __init__(self, shuffle=False):
    self.widgets = {}
    self.in_game = False
    self.shuffle = shuffle
    
    # Set up the frame
    self.root = tk.Tk()
    self.frame = tk.Frame(self.root, width=0, height=0)
    
    # bind buttons to specific methods
    
    ''' begin or end game '''
    self.frame.bind('<Return>', self.start_game)
    self.frame.pack()
    self.frame.bind('<Escape>', self.quit_game)
    self.frame.pack()
    
    ''' rotate cube clockwise'''
    self.frame.bind('<Up>', self.rot_upper_clock)
    self.frame.pack()
    self.frame.bind('<Down>', self.rot_bottom_clock)
    self.frame.pack()
    self.frame.bind('<Left>', self.rot_left_clock)
    self.frame.pack()
    self.frame.bind('<Right>', self.rot_right_clock)
    self.frame.pack()
    self.frame.bind('<space>', self.rot_front_clock)
    self.frame.pack()
    
    ''' rotate cube counterclockwise'''
    self.frame.bind('<Shift-Up>', self.rot_upper_cntclck)
    self.frame.pack()
    self.frame.bind('<Shift-Down>', self.rot_bottom_cntclck)
    self.frame.pack()
    self.frame.bind('<Shift-Left>', self.rot_left_cntclck)
    self.frame.pack()
    self.frame.bind('<Shift-Right>', self.rot_right_cntclck)
    self.frame.pack()
    self.frame.bind('<Shift-space>', self.rot_front_cntclck)
    self.frame.pack()
    
    ''' rotate cube view '''
    self.frame.bind('<Control-Up>', self.rot_cube_view_up)
    self.frame.pack()
    self.frame.bind('<Control-Down>', self.rot_cube_view_down)
    self.frame.pack()
    self.frame.bind('<Control-Left>', self.rot_cube_view_left)
    self.frame.pack()
    self.frame.bind('<Control-Right>', self.rot_cube_view_right)
    self.frame.pack()
    self.frame.bind('<Control-space>', self.rot_cube_view_clockwise)
    self.frame.pack()
    self.frame.bind('<Control-Shift-space>', self.rot_cube_view_cntclockwise)
    self.frame.pack()
    
    # print the load/start screen
    self.text=print_start_screen()
    self.label=tk.Label(self.root, anchor='w', justify='left', text=self.text, font=('Consolas', 10))
    self.label.pack(fill='both', expand=1)
    
    # This call gives the frame focus so that it receives input.
    self.frame.focus_set()
    
    self.root.mainloop()
  
  def clear(self):
    self.label.destroy()
    
  def quit(self):
    self.root.destroy()
    
  
  """ rotate cube sides clockwise """
  def start_game(self,event):
    if not self.in_game:
      self.clear()

      # print start screen
      self.current_cube = self.game_cube.r_cube
      self.text=print_cube(self.current_cube)
      self.label=tk.Label(self.root, anchor='w', justify='left', text=self.text, font=('Consolas', 10))
      self.label.pack()
    
      # TODO: mix cube - 10 random turns, print screen after each
      if self.shuffle:
        for i in range(10):
          rand_f=random.randint(0,9)
          if rand_f==0:
            self.rot_upper_clock(event)
          elif rand_f==1:
            self.rot_bottom_clock(event)
          elif rand_f==2:
            self.rot_left_clock(event)
          elif rand_f==3:
            self.rot_right_clock(event)
          elif rand_f==4:
            self.rot_front_clock(event)
          elif rand_f==5:
            self.rot_upper_cntclck(event)
          elif rand_f==6:
            self.rot_bottom_cntclck(event)
          elif rand_f==7:
            self.rot_left_cntclck(event)
          elif rand_f==8:
            self.rot_right_cntclck(event)
          else: 
            self.rot_front_cntclck(event)
      self.in_game=True
    
    
  def quit_game(self, event):
    # if in game, hitting 'esc' prints game-over
    if self.in_game:
      self.clear()
      self.text=print_end_screen()
      self.label=tk.Label(self.root, anchor='w', justify='left', text=self.text, font=('Consolas', 12))
      self.label.pack()
      
      # change status to not-in-game
      self.in_game=False
    
    # if not in game, hitting 'esc' exits
    else:
      self.quit()
    
  def rot_upper_clock(self, event):
    self.game_cube.rot_upper()
    self.clear()
    self.text=print_cube(self.game_cube.r_cube)
    self.label=tk.Label(self.root, anchor='w', justify='left', text=self.text, font=('Consolas', 10))
    self.label.pack()

  def rot_bottom_clock(self, event):
    self.game_cube.rot_bottom()
    self.clear()
    self.text=print_cube(self.game_cube.r_cube)
    self.label=tk.Label(self.root, anchor='w', justify='left', text=self.text, font=('Consolas', 10))
    self.label.pack()

  def rot_left_clock(self, event):
    self.game_cube.rot_left()
    self.clear()
    self.text=print_cube(self.game_cube.r_cube)
    self.label=tk.Label(self.root, anchor='w', justify='left', text=self.text, font=('Consolas', 10))
    self.label.pack()
    
  def rot_right_clock(self, event):
    self.game_cube.rot_right()
    self.clear()
    self.text=print_cube(self.game_cube.r_cube)
    self.label=tk.Label(self.root, anchor='w', justify='left', text=self.text, font=('Consolas', 10))
    self.label.pack()
    
  def rot_front_clock(self, event):
    self.game_cube.rot_front()
    self.clear()
    self.text=print_cube(self.game_cube.r_cube)
    self.label=tk.Label(self.root, anchor='w', justify='left', text=self.text, font=('Consolas', 10))
    self.label.pack()
    
  ''' rotate cube sides clockwise '''
  
  def rot_upper_cntclck(self, event):
    self.game_cube.rot_upper_cntr()
    self.clear()
    self.text=print_cube(self.game_cube.r_cube)
    self.label=tk.Label(self.root, anchor='w', justify='left', text=self.text, font=('Consolas', 10))
    self.label.pack()
  
  def rot_bottom_cntclck(self, event):
    self.game_cube.rot_bottom_cntr()
    self.clear()
    self.text=print_cube(self.game_cube.r_cube)
    self.label=tk.Label(self.root, anchor='w', justify='left', text=self.text, font=('Consolas', 10))
    self.label.pack()
  
  def rot_left_cntclck(self, event):
    self.game_cube.rot_left_cntr()
    self.clear()
    self.text=print_cube(self.game_cube.r_cube)
    self.label=tk.Label(self.root, anchor='w', justify='left', text=self.text, font=('Consolas', 10))
    self.label.pack()
  
  def rot_right_cntclck(self, event):
    self.game_cube.rot_right_cntr()
    self.clear()
    self.text=print_cube(self.game_cube.r_cube)
    self.label=tk.Label(self.root, anchor='w', justify='left', text=self.text, font=('Consolas', 10))
    self.label.pack()
  
  def rot_front_cntclck(self, event):
    self.game_cube.rot_front_cntr()
    self.clear()
    self.text=print_cube(self.game_cube.r_cube)
    self.label=tk.Label(self.root, anchor='w', justify='left', text=self.text, font=('Consolas', 10))
    self.label.pack()
      
  """ TODO: add ability to rotate view of cube """
  
  def rot_cube_view_up(self, event):
    self.clear()
    print('rot up')
    
  def rot_cube_view_down(self, event):
    self.clear()
    print('rot dow')
  
  def rot_cube_view_left(self, event):
    self.clear()
    print('rot left')
  
  def rot_cube_view_right(self, event):
    self.clear()
    print('rot right')
  
  def rot_cube_view_clockwise(self, event):
    self.clear()
    print('rot clckws')
  
  def rot_cube_view_cntclockwise(self, event):
    self.clear()
    print('rot cntclckws')
    
  
if __name__ == "__main__":
  KeyControls2x2()