### This code turns our image green, and adds a border.

from PIL import Image
import colours

# Constants.
# 10 corresponds to one tenth.
center_proportion = 10
acceptable_yellow = 0.7

class Splodgifier:
  # Fields.
  input_image = None
  img = None
  pxx = None
  out = None
  # 0 = unchecked, 1 = not over land, 2 = over land
  over_land_flag = 0

  # Setters.
  def set_input_image(self, s):
    self.over_land_flag = 0
    self.input_image = s
  def set_img(self):
    self.img = Image.open(self.input_image)
  def set_pxx(self):
    self.pxx = self.img.load()
  def set_out(self, s):
    self.out = s
  def set_all(self, s1, s2):
    self.set_input_image(s1)
    self.set_img()
    self.set_pxx()
    self.set_out(s2)

  # Checks whether the chart is showing our position as
  # over land.
  def check_over_land(self):
    yellow_pxx = 0
    total_pxx = ((self.img.size[0]/center_proportion)*
                 (self.img.size[1]/center_proportion))
    center0 = self.img.size[0]/2
    center1 = self.img.size[1]/2
    start0 = (center0-
              (self.img.size[0]/(center_proportion*2)))
    end0 = (center0+
            (self.img.size[0]/(center_proportion*2)))
    start1 = (center1-
              (self.img.size[1]/(center_proportion*2)))
    end1 = (center1+
            (self.img.size[1]/(center_proportion*2)))
    if(self.over_land_flag == 1):
      return
    elif(self.over_land_flag == 2):
      return
    else:
      for i in range(start0, end0):
        for j in range(start1, end1):
          if(colours.is_yellow(self.pxx[i, j])):
            yellow_pxx = yellow_pxx+1
      if(float(yellow_pxx)/float(total_pxx) > acceptable_yellow):
        self.over_land_flag = 2
      else:
        self.over_land_flag = 1

  # Ronseal.
  def turn_green(self):
    for i in range(self.img.size[0]):
      for j in range(self.img.size[1]):
        if(colours.is_not_white(self.pxx[i, j])):
          self.pxx[i, j] = colours.green

  # Ronseal.
  def turn_yellow(self):
    for i in range(self.img.size[0]):
      for j in range(self.img.size[1]):
        if(colours.is_not_white(self.pxx[i, j])):
          self.pxx[i, j] = colours.yellow

  # These functions draw an edge round our image.
  def colour_left_edge(self):
    for i in range(self.img.size[0]-1):
      for j in range(self.img.size[1]):
        if(colours.is_white(self.pxx[i, j]) and
           colours.is_yellow(self.pxx[i+1, j])):
          self.pxx[i, j] = colours.green

  def colour_right_edge(self):
    for i in range(1, self.img.size[0]):
      for j in range(self.img.size[1]):
        if(colours.is_white(self.pxx[i, j]) and
           colours.is_yellow(self.pxx[i-1, j])):
          self.pxx[i, j] = colours.green

  def colour_top_edge(self):
    for i in range(self.img.size[0]):
      for j in range(self.img.size[1]-1):
        if(colours.is_white(self.pxx[i, j]) and
           colours.is_yellow(self.pxx[i, j+1])):
          self.pxx[i, j] = colours.green

  def colour_bottom_edge(self):
    for i in range(self.img.size[0]):
      for j in range(1, self.img.size[1]):
        if(colours.is_white(self.pxx[i, j]) and
           colours.is_yellow(self.pxx[i, j-1])):
          self.pxx[i, j] = colours.green

  def colour_edges(self):
    self.colour_left_edge()
    self.colour_right_edge()
    self.colour_top_edge()
    self.colour_bottom_edge()

  # Ronseal.
  def save_to_out(self):
    self.img.save(self.out)

  # Wraps up the "splodgification" into one function.
  def splodgify(self):
    self.check_over_land()
    self.turn_yellow()
    self.colour_edges()
    self.turn_green()

# This will require the presence of tshape.png in this
# directory in order to work.
def demo():
  program = Splodgifier()
  program.set_all("noblack_simplified_chart_test1.png",
                  "splodges.png")
  program.splodgify()
  program.save_to_out()

# demo()
