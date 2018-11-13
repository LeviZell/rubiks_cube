import numpy as np
import tkinter as tk
import random
from rubiks_print_2x2 import *


class RubiksCube2x2:
  """
  Class for interacting with a Rubik's Cube  
  
  Methods: 
    load_cube
    mix_up_cube
    
    manipulate cube:
      rot_left
      rot_right
      rot_upper
      rot_bottom
      rot_front
    
    checks:
      is_complete
      
  """
  color_key={0:'whi', 1:'gre', 2:'blu', 3:'org', 4:'red', 5:'yel'}
  
  def __init__ (self, r_cube=np.zeros(shape=(6,2,2)), color_key={}):
    self.r_cube = r_cube
    self.color_key = color_key
        
    self.in_game=False
    
    self.r_cube = np.array([[[0, 0],  # white - top
                            [0, 0]],

                           [[1, 1],    # green - front
                            [1, 1]],

                           [[2, 2],    # blue - back
                            [2, 2]],

                           [[3, 3],    # orange - left
                            [3, 3]],

                           [[4, 4],    # red - right
                            [4, 4]],

                           [[5, 5],    # yellow - bottom
                            [5, 5]]])
      
    
  ''' rotate cube clockwise '''
  def rot_right(self):
    r_new = np.copy(self.r_cube)
    
    r_new[0][1, :] = self.r_cube[1][1, :]
    r_new[1][1, :] = self.r_cube[5][1, :]
    r_new[5][1, :] = self.r_cube[2][1, :]
    r_new[2][1, :] = self.r_cube[0][1, :]
    
    # rotate right face clockwise:
    r_new = RubiksCube2x2.rot_clock(r_new, 4)

    self.r_cube= np.copy(r_new)
  
  def rot_left(self):
    r_new = np.copy(self.r_cube)
    
    r_new[0][0, :] = self.r_cube[2][0, :]
    r_new[2][0, :] = self.r_cube[5][0, :]
    r_new[5][0, :] = self.r_cube[1][0, :]
    r_new[1][0, :] = self.r_cube[0][0, :]
    
    # rotate left face clockwise:
    r_new = RubiksCube2x2.rot_clock(r_new, 3)

    self.r_cube= np.copy(r_new)
  
  def rot_upper(self):
    r_new = np.copy(self.r_cube)
    
    r_new[1][:, 0] = self.r_cube[4][:, 0]
    r_new[4][:, 0] = self.r_cube[2][:, 0]
    r_new[2][:, 0] = self.r_cube[3][:, 0]
    r_new[3][:, 0] = self.r_cube[1][:, 0]
    
    # rotate top face clockwise:
    r_new = RubiksCube2x2.rot_clock(r_new, 0)

    self.r_cube= np.copy(r_new)
      
  def rot_bottom(self):
    r_new = np.copy(self.r_cube)
    
    r_new[1][:, 1] = self.r_cube[3][:, 1]
    r_new[3][:, 1] = self.r_cube[2][:, 1]
    r_new[2][:, 1] = self.r_cube[4][:, 1]
    r_new[4][:, 1] = self.r_cube[1][:, 1]
    
    # rotate bottom face clockwise:
    r_new = RubiksCube2x2.rot_clock(r_new, 5)

    self.r_cube= np.copy(r_new)  
    
  def rot_front(self):
    r_new = np.copy(self.r_cube)
    
    r_new[0][:, 1] = self.r_cube[3][1, :]
    r_new[3][1, :] = self.r_cube[5][:, 0]
    r_new[5][:, 0] = self.r_cube[4][0, :]
    r_new[4][0, :] = self.r_cube[0][:, 1]
    
    # rotate bottom face clockwise:
    r_new = RubiksCube2x2.rot_clock(r_new, 1)

    self.r_cube= np.copy(r_new)  
  
  def rot_clock(cube, i):
    # rotate the face of side i clockwise
    r_new = np.copy(cube)
    
    r_new[i][0, 0] = cube[i][0, 1]
    r_new[i][0, 1] = cube[i][1, 1]
    r_new[i][1, 1] = cube[i][1, 0]
    r_new[i][1, 0] = cube[i][0, 0]
    
    return r_new
  
  
  ''' 
  rotate cube counterclockwise 
  '''
  
  def rot_right_cntr(self):
    r_new = np.copy(self.r_cube)
    
    r_new[0][1, :] = self.r_cube[2][1, :]
    r_new[2][1, :] = self.r_cube[5][1, :]
    r_new[5][1, :] = self.r_cube[1][1, :]
    r_new[1][1, :] = self.r_cube[0][1, :]
    
    # rotate right face counterclockwise:
    r_new = RubiksCube2x2.rot_cntclock(r_new, 4)

    self.r_cube= np.copy(r_new)
  
  def rot_left_cntr(self):
    r_new = np.copy(self.r_cube)
    
    r_new[0][0, :] = self.r_cube[1][0, :]
    r_new[1][0, :] = self.r_cube[5][0, :]
    r_new[5][0, :] = self.r_cube[2][0, :]
    r_new[2][0, :] = self.r_cube[0][0, :]
    
    # rotate left face counterclockwise:
    r_new = RubiksCube2x2.rot_cntclock(r_new, 3)

    self.r_cube= np.copy(r_new)
  
  def rot_upper_cntr(self):
    r_new = np.copy(self.r_cube)
    
    r_new[1][:, 0] = self.r_cube[3][:, 0]
    r_new[3][:, 0] = self.r_cube[2][:, 0]
    r_new[2][:, 0] = self.r_cube[4][:, 0]
    r_new[4][:, 0] = self.r_cube[1][:, 0]
    
    # rotate top face counterclockwise:
    r_new = RubiksCube2x2.rot_cntclock(r_new, 0)

    self.r_cube= np.copy(r_new)
      
  def rot_bottom_cntr(self):
    r_new = np.copy(self.r_cube)
    
    r_new[1][:, 1] = self.r_cube[4][:, 1]
    r_new[4][:, 1] = self.r_cube[2][:, 1]
    r_new[2][:, 1] = self.r_cube[3][:, 1]
    r_new[3][:, 1] = self.r_cube[1][:, 1]
    
    # rotate bottom face counterclockwise:
    r_new = RubiksCube2x2.rot_cntclock(r_new, 5)

    self.r_cube= np.copy(r_new)  
    
  def rot_front_cntr(self):
    r_new = np.copy(self.r_cube)
    
    r_new[0][:, 1] = self.r_cube[4][0, :]
    r_new[4][0, :] = self.r_cube[5][:, 0]
    r_new[5][:, 0] = self.r_cube[3][1, :]
    r_new[3][1, :] = self.r_cube[0][:, 1]
    
    # rotate bottom face counterclockwise:
    r_new = RubiksCube2x2.rot_cntclock(r_new, 1)

    self.r_cube= np.copy(r_new)
    
  def rot_cntclock(cube, i):
    # rotate the face of side i counterclockwise
    r_new = np.copy(cube)
    
    r_new[i][0, 0] = cube[i][1, 0]
    r_new[i][1, 0] = cube[i][1, 1]
    r_new[i][1, 1] = cube[i][0, 1]
    r_new[i][0, 1] = cube[i][0, 0]
          
    return r_new
            
  ''' Checks '''
  def is_complete(self):
    # check all faces on w, b, y, r, or g side match center face 
    return all(item==True for item in [np.all(r_cube[i]==r_cube[i][0,0]) for i in range(6)])

