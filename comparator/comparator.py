### This code compares the splodges in (1) and (2).

from shutil import copyfile
from PIL import Image
import os

import splodgifier
import colours

# Constants.
min_grnn = 50

class Comparator:
  # Fields.
  spfr = splodgifier.Splodgifier()
  input_image1 = None
  img1 = None
  pxx1 = None
  input_image2 = None
  img2 = None
  pxx2 = None
  splodgifactions = 1
  splodgified = None
  grnn = 0
  diff = 0
  original = None
  min_grnn_flag = 0
  over_land_flag = 0

  # Setters.
  def set_input_image1(self, s):
    self.input_image1 = s
  def set_img1(self):
    self.img1 = Image.open(self.input_image1)
  def set_pxx1(self):
    self.pxx1 = self.img1.load()
  def set_input_image2(self, s):
    self.input_image2 = s
  def set_img2(self):
    self.img2 = Image.open(self.input_image2)
  def set_pxx2(self):
    self.pxx2 = self.img2.load()
  def set_splodgifactions(self, n):
    self.splodgifactions = n
  def set_splodgified(self):
    if(self.input_image2 == None):
      return
    else:
      self.splodgified = ("splodgified_"+
                          str(self.splodgifactions)+
                          "times_"+self.input_image2)
  def set_all(self, s1, s2, n):
    self.set_input_image1(s1)
    self.set_input_image2(s2)
    self.set_img1()
    self.set_img2()
    self.set_pxx1()
    self.set_pxx2()
    self.set_splodgifactions(n)
  def set_original(self, s):
    self.original = s

  # Checks whether the proportion of green pixels is above the
  # agreed minimum.
  def check_gp(self, gp):
    self.min_grnn_flag = 0
    if(gp == 0):
      self.min_grnn_flag = 1
      return
    tp = self.img1.size[0]*self.img1.size[1]
    r = tp/gp
    if(r > min_grnn):
      self.min_grnn_flag = 1

  # Ronseal
  def splodgify(self):
    self.set_splodgified()
    self.set_original(self.input_image2)
    copyfile(self.input_image2, self.splodgified)
    self.spfr.set_all(self.splodgified, self.splodgified)
    for i in range(0, self.splodgifactions):
      self.spfr.splodgify()
      self.spfr.save_to_out()
    if(self.spfr.over_land_flag == 2):
      self.over_land_flag = 1
    else:
      self.over_land_flag = 0
    self.set_all(self.input_image1, self.splodgified,
                 self.splodgifactions)

  # Calculates the "grnn" and "diff" fields.
  def update_grnn_diff(self):
    self.grnn = 0;
    self.diff = 0;
    if(self.img1.size[0] != self.img2.size[0]):
      print("Images not the same width.")
      return
    if(self.img1.size[1] != self.img2.size[1]):
      print("Images not the same height.")
      return
    for i in range(self.img1.size[0]):
      for j in range(self.img1.size[1]):
        if(colours.is_green(self.pxx1[i, j])):
          self.grnn += 1
          if(colours.is_not_green(self.pxx2[i, j])):
            self.diff += 1
    self.check_gp(self.grnn)

  # Finds the percentage match between the two images.
  def match(self):
    self.splodgify()
    self.update_grnn_diff()
    os.remove(self.splodgified)

  # Prints the results of "match".
  def print_match(self):
    if(self.original == None):
      self.set_original(self.input_image2)
    self.match()
    print("Comparing "+self.input_image1+" and "+
          self.original+" with "+str(self.splodgifactions)+
          " splodgifactions...")
    print(str(self.diff)+" pixels not accounted for.")

# test()
# demo()
