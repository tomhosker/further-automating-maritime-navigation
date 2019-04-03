### This code simplifies the colours in our chart image.

from PIL import Image
import colours

class Black_remover:
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
    self.output = "noblack_"+self.input_image
  def set_all(self, s):
    self.set_input_image(s)
    self.set_img()
    self.set_pxx()
    self.set_output()

  # Getter.
  def save_to_output(self):
    self.img.save(self.output)

  # Ronseal.
  def remove_black(self):
    for i in range(self.img.size[0]):
      for j in range(self.img.size[1]):
        pixel = self.pxx[i, j]
        right = colours.black
        up = colours.black
        left = colours.black
        down = colours.black
        if(j != self.img.size[1]-1):
          right = self.pxx[i, j+1]
        if(i != 0):
          up = self.pxx[i-1, j]
        if(j != 0):
          left = self.pxx[i, j-1]
        if(i != self.img.size[0]-1):
          down = self.pxx[i+1, j]
        if(colours.is_black(pixel)):
          if(colours.is_yellow(right)):
            self.pxx[i, j] = colours.yellow
          elif(colours.is_white(right)):
            self.pxx[i, j] = colours.white
          elif(colours.is_yellow(up)):
            self.pxx[i, j] = colours.yellow
          elif(colours.is_white(up)):
            self.pxx[i, j] = colours.white
          elif(colours.is_white(left)):
            self.pxx[i, j] = colours.white
          elif(colours.is_yellow(left)):
            self.pxx[i, j] = colours.yellow
          elif(colours.is_white(down)):
            self.pxx[i, j] = colours.white
          elif(colours.is_yellow(down)):
            self.pxx[i, j] = colours.yellow

  # Tests whether the image still contains any black pixels.
  def contains_black(self):
    for i in range(self.img.size[0]):
      for j in range(self.img.size[1]):
        if(colours.is_black(self.pxx[i, j])):
          return(True)
    return(False)

  # Runs the unit tests.
  # For this to work, the correct test files must be present
  # in this directory.
  def test(self):
    self.set_all("simplified_chart_test1.png")
    self.remove_black()
    assert(self.contains_black() == False)
    print("Tests passed!")

  # Runs a demo.
  # For this to work, the correct test files must be present
  # in this directory.
  def demo(self):
    self.set_all("simplified_chart_test1.png")
    self.remove_black()
    self.save_to_output()

def test():
  program = Black_remover()
  program.test()

def demo():
  program = Black_remover()
  program.demo()

# test()
# demo()
