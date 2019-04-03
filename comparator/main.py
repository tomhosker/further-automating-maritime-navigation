### This code compares the splodges in (1) against the chart
### in (2).

from shutil import copyfile
from PIL import Image
import os

import colours
import timeit
import image_processor
import comparator

# Constants.
goodness_cutoff = 10000
# pp stands for "Processed Prefix".
pp = "noblack_simplified_"

class Main:
  # Fields.
  impsr = image_processor.Image_processor()
  cmptr = comparator.Comparator()

  input_source1 = None
  input_source2 = None
  radar = None
  chart = None
  splodgifactions = 1
  diff = 0
  result = 0

  # Setters.
  def set_input_source1(self, s):
    self.input_source1 = s
  def set_input_source2(self, s):
    self.input_source2 = s
  def set_radar(self):
    self.radar = "radar.png"
    copyfile(self.input_source1, self.radar)
  def set_chart(self):
    self.chart = "chart.png"
    copyfile(self.input_source2, self.chart)
  def set_splodgifactions(self, n):
    self.splodgifactions = n
  def set_all(self, s1, s2, n):
    self.set_input_source1(s1)
    self.set_input_source2(s2)
    self.set_radar()
    self.set_chart()
    self.set_splodgifactions(n)

  # Converts our "result" code into a sentence in English.
  def print_result(self):
    if(self.result == 0):
      print("GPS verified.")
    elif(self.result == 1):
      print("GPS falsified.")
    else:
      print("Too little data.")

  # Ronseal.
  def run_full_comparison(self, s1, s2, n):
    self.set_all(s1, s2, n)
    self.impsr.set_all(self.chart)
    self.impsr.process()
    self.chart = pp+self.chart
    self.cmptr.set_all(self.radar,
                       self.chart,
                       self.splodgifactions)
    self.cmptr.match()
    os.remove(self.chart)
    self.diff = self.cmptr.diff
    if(self.cmptr.over_land_flag == 1):
      print("Over land by GPS!")
      self.result = 1
      return
    elif(self.cmptr.min_grnn_flag == 1):
      self.result = 2
    else:
      self.result = 0
    if(self.result == 2):
      return
    elif(self.diff > goodness_cutoff):
      self.result = 1
    else:
      self.result = 0

  # Ronseal.
  def print_full_comparison(self, s1, s2, n):
    print("Comparing "+s1+" and "+s2+" with "+
          str(n)+" splodgifactions...")
    self.run_full_comparison(s1, s2, n)
    print("diff = "+str(self.diff))
    self.print_result()

  # Runs the unit tests.
  # For this to work, the correct test files must be present
  # in this directory.
  def test(self):
    print("Running unit tests...")
    self.run_full_comparison("test0.png", "chart_test1.png", 1)
    assert(self.diff == 0)
    self.run_full_comparison("test1.png", "chart_test1.png", 1)
    assert(self.result == 0)
    self.run_full_comparison("test2.png", "chart_test2.png", 1)
    assert(self.result == 1)
    self.run_full_comparison("test3.png", "chart_test3.png", 1)
    assert(self.result == 2)
    print("Tests passed!")

  # Runs a demo.
  # For this to work, the correct test files must be present
  # in this directory.
  def demo(self):
    self.print_full_comparison("radar_good/1.png",
                               "charts_good/1.png", 1)

  # Runs the simulation.
  def run_sim(self):
    current_radar = None
    current_chart = None
    for i in range(1, 31):
      current_radar = "radar_good/"+str(i)+".png"
      current_chart = "charts_good/"+str(i)+".png"
      self.print_full_comparison(current_radar,
                                 current_chart, 1)
      print("")

def test():
  program = Main()
  program.test()

def demo():
  start = timeit.default_timer()
  program = Main()
  program.demo()
  stop = timeit.default_timer()
  print("Time taken to run demo: "+str(stop-start)+
        " seconds.")

def run_sim():
  program = Main()
  program.run_sim()

# test()
demo()
# run_sim()
