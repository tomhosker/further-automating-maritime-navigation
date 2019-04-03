### This code simplifies the colours in our chart image.

from PIL import Image
import colours

class Simplifier:
  # Fields.
  input_image = None
  img = None
  pxx = None
  output = None

  # Setters.
  def set_input_image(self, s):
    self.input_image = s
  def set_img(self):
    self.img = Image.open(self.input_image)
  def set_pxx(self):
    self.pxx = self.img.load()
  def set_output(self):
    self.output = "simplified_"+self.input_image
  def set_all(self, s):
    self.set_input_image(s)
    self.set_img()
    self.set_pxx()
    self.set_output()

  # Getter.
  def save_to_output(self):
    self.img.save(self.output)

  # Converts each pixel to either yellow, white or black.
  def simplify(self):
    for i in range(self.img.size[0]):
      for j in range(self.img.size[1]):
        pixel = self.pxx[i, j]
        if(colours.is_land0(pixel)):
          self.pxx[i, j] = colours.yellow
        elif(colours.is_land1(pixel)):
          self.pxx[i, j] = colours.yellow
        elif(colours.is_drying(pixel)):
          self.pxx[i, j] = colours.white
        elif(colours.is_water0(pixel)):
          self.pxx[i, j] = colours.white
        elif(colours.is_water1(pixel)):
          self.pxx[i, j] = colours.white
        else:
          self.pxx[i, j] = colours.black

  # Runs the unit tests.
  # For this to work, the correct test files must be present
  # in this directory.
  def test(self):
    self.set_all("chart_test1.png")
    self.simplify()
    self.img.save("simplified_chart_test1.png")
    self.set_all("simplified_chart_test1.png")
    for i in range(self.img.size[0]):
      for j in range(self.img.size[1]):
        assert((self.pxx[i, j] == colours.white) or
               (self.pxx[i, j] == colours.yellow) or
               (self.pxx[i, j] == colours.black))
    print("Tests passed!")

  # Runs a demo.
  # For this to work, the correct test files must be present
  # in this directory.
  def demo(self):
    self.set_all("chart_test1.png")
    self.simplify()
    self.img.save("simplified_chart_test1.png")

def test():
  program = Simplifier()
  program.test()

def demo():
  program = Simplifier()
  program.demo()

# test()
# demo()
