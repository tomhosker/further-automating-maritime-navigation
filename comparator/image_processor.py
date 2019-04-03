### This code processes our chart image.

from PIL import Image
import os

import colours
import simplifier
import black_remover

class Image_processor:
  # Fields.
  simp = simplifier.Simplifier()
  blck = black_remover.Black_remover()
  input_image = None
  img = None
  pxx = None

  # Setters.
  def set_input_image(self, s):
    self.input_image = s
  def set_img(self):
    self.img = Image.open(self.input_image)
  def set_img_dash(self, new_img):
    self.img = new_img
  def set_pxx(self):
    self.pxx = self.img.load()
  def set_pxx_dash(self, new_pxx):
    self.pxx = new_pxx
  def set_all(self, s):
    self.set_input_image(s)
    self.set_img()
    self.set_pxx()

  # Ronseal.
  def simplify_it(self):
    self.simp.set_all(self.input_image)
    self.simp.simplify()
    self.simp.save_to_output()

  # Ronseal.
  def remove_black_from_it(self):
    simplified = "simplified_"+self.input_image
    self.blck.set_all(simplified)
    self.blck.remove_black()
    self.blck.save_to_output()
    os.remove(simplified)

  # Ronseal.
  def process(self):
    self.simplify_it()
    self.remove_black_from_it()

  # Runs a demo.
  # For this to work, the correct test files must be present
  # in this directory.
  def demo(self):
    self.set_all("chart_test1.png")
    self.process()

def demo():
  program = Image_processor()
  program.demo()

# demo()
