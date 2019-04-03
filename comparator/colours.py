# Colours. The final 255 is for opacity.
white = (255, 255, 255, 255)
black = (0, 0, 0, 255)
yellow = (255, 255, 0, 255)
green = (0, 255, 0, 255)
light_green = (127, 255, 127, 255)

# Other constants.
def full():
  return(255)

# Determines whether a given pixel is WHITE.
def is_white(pixel):
  if(pixel[0] != 255):
    return(False)
  if(pixel[1] != 255):
    return(False)
  if(pixel[2] != 255):
    return(False)
  return(True)

# Determines whether a given pixel is NOT WHITE.
def is_not_white(pixel):
  if(pixel[0] != 255):
    return(True)
  if(pixel[1] != 255):
    return(True)
  if(pixel[2] != 255):
    return(True)
  return(False)

# Determines whether a given pixel is BLACK.
def is_black(pixel):
  if(pixel[0] != 0):
    return(False)
  if(pixel[1] != 0):
    return(False)
  if(pixel[2] != 0):
    return(False)
  return(True)

# Determines whether a given pixel is GREEN.
def is_green(pixel):
  if(pixel[0] != 0):
    return(False)
  if(pixel[1] != 255):
    return(False)
  if(pixel[2] != 0):
    return(False)
  return(True)

# Determines whether a given pixel is NOT GREEN.
def is_not_green(pixel):
  if(pixel[0] != 0):
    return(True)
  if(pixel[1] != 255):
    return(True)
  if(pixel[2] != 0):
    return(True)
  return(False)

# Determines whether a given pixel is YELLOW.
def is_yellow(pixel):
  if(pixel[0] != 255):
    return(False)
  if(pixel[1] != 255):
    return(False)
  if(pixel[2] != 0):
    return(False)
  return(True)

# Determines whether a given pixel represents LAND.
def is_land0(pixel):
  if(not(170 <= pixel[0] <= 180)):
    return(False)
  if(not(140 <= pixel[1] <= 150)):
    return(False)
  if(not(50 <= pixel[2] <= 60)):
    return(False)
  return(True)

# Also determines whether a given pixel represents LAND.
def is_land1(pixel):
  if(not(200 <= pixel[0] <= 210)):
    return(False)
  if(not(180 <= pixel[1] <= 190)):
    return(False)
  if(not(120 <= pixel[2] <= 130)):
    return(False)
  return(True)

# Determines whether a given pixel represents a DRYING HEIGHT.
def is_drying(pixel):
  if(not(130 <= pixel[0] <= 140)):
    return(False)
  if(not(170 <= pixel[1] <= 180)):
    return(False)
  if(not(140 <= pixel[2] <= 150)):
    return(False)
  return(True)

# Determines whether a given pixel represents WATER.
def is_water0(pixel):
  if(not(110 <= pixel[0] <= 120)):
    return(False)
  if(not(180 <= pixel[1] <= 190)):
    return(False)
  if(not(230 <= pixel[2] <= 240)):
    return(False)
  return(True)

# Also determines whether a given pixel represents WATER.
def is_water1(pixel):
  if(pixel[0] < 240):
    return(False)
  if(pixel[1] < 240):
    return(False)
  if(pixel[2] < 240):
    return(False)
  return(True)
