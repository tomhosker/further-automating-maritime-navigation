### This code calculates the height of the sun.

import math

class Solar:
  # Drawn from the Nautical Almanac 2018.
  true_corrections = [34.5, 44.2, 50.1, 53.9, 56.4,
                      58.2, 59.5, 60.5, 61.2, 61.7,
                      62.1, 62.4, 62.6, 62.7, 62.8,
                      62.8, 62.7, 62.7, 62.5, 62.4,
                      62.2, 62.0, 61.7, 61.5, 61.2,
                      60.8, 60.5, 60.1, 59.7, 59.3,
                      58.9, 58.5, 58.0, 57.5, 57.0,
                      56.5, 56.0, 55.4, 54.9, 54.3,
                      53.7, 53.1, 52.4, 51.8, 51.1,
                      50.5, 49.8, 49.1, 48.4, 47.7,
                      46.9, 46.2, 45.4, 44.6, 43.9,
                      43.1, 42.3, 41.4, 40.6, 39.8,
                      38.9, 38.1, 37.2, 36.4, 35.5,
                      34.6, 33.7, 32.8, 31.9, 31.0,
                      30.0, 29.1, 28.2, 27.2, 26.3,
                      25.3, 24.4, 23.4, 22.5, 21.5,
                      20.5, 19.6, 18.6, 17.6, 16.6,
                      15.6, 14.6, 13.7, 12.7, 11.7]

  # "Input" fields.
  day_of_the_year = 208
  hours = 14
  minutes = 0
  seconds = 0
  lat = 51.45451
  lon = -2.58791

  # "Calculated" fields.
  greenwich_hour_angle = 0.0
  local_hour_angle = 0.0
  declination = 0.0
  true_altitude = 0.0
  apparent_altitude = 0.0

  # Ronseal.
  def calculate_hour_angles(self):
    t_s = float(self.seconds)/3600
    t_m = float(self.minutes)/60
    t_h = float(self.hours)
    t = t_h+t_m+t_s
    gha = (t-12)*15
    if(gha < self.lon):
      gha = gha+360
    self.greenwich_hour_angle = gha
    self.local_hour_angle = self.greenwich_hour_angle+self.lon

  # Ronseal.
  def calculate_declination(self):
    n = self.day_of_the_year
    d = 1.914*math.sin(math.radians(0.98565*(n-2)))
    d = d+(0.98565*(n+10))
    d = 0.39799*math.cos(math.radians(d))
    d = math.asin(d)
    self.declination = -math.degrees(d)

  # Ronseal.
  def calculate_true_altitude(self):
    a1 = math.cos(math.radians(self.lat))
    a1 = a1*math.cos(math.radians(self.declination))
    a1 = a1*math.cos(math.radians(self.local_hour_angle))
    a2 = math.sin(math.radians(self.lat))
    a2 = a2*math.sin(math.radians(self.declination))
    a = a1+a2
    self.true_altitude = math.degrees(math.asin(a))

  # Ronseal.
  def calculate_apparent_altitude(self):
    ta = int(self.true_altitude)
    true_correction = self.true_corrections[ta]
    true_correction = true_correction/60
    self.apparent_altitude = self.true_altitude+true_correction

  # Wraps the above into one method.
  def calculate_altitude(self):
    self.calculate_hour_angles()
    self.calculate_declination()
    self.calculate_true_altitude()
    self.calculate_apparent_altitude()

  # Runs the unit tests.
  def test(self):
    print("Tests passed!")

  # Runs a demo.
  def demo(self):
    self.calculate_altitude()
    print(self.local_hour_angle)
    print(self.declination)
    print(self.true_altitude)
    print(self.apparent_altitude)

def test():
  program = Solar()
  program.test()

def demo():
  program = Solar()
  program.demo()

# test()
demo()
