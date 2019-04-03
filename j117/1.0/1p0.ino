#include <SparkFun_ADXL345.h>

ADXL345 adxl = ADXL345(10);


void setup()
{
  Serial.begin(9600);
  adxl.powerOn();
  adxl.setRangeSetting(16);
  adxl.setSpiBit(0);
  adxl.setActivityXYZ(1, 0, 0);
  adxl.setActivityThreshold(75);
  adxl.setInactivityXYZ(1, 0, 0);
  adxl.setInactivityThreshold(75);
  adxl.setTimeInactivity(10);
  adxl.setTapDetectionOnXYZ(0, 0, 1);
  adxl.setTapThreshold(50);
  adxl.setTapDuration(15);
  adxl.setDoubleTapLatency(80);
  adxl.setDoubleTapWindow(200);
  adxl.setFreeFallThreshold(7);
  adxl.setFreeFallDuration(30);
  adxl.InactivityINT(1);
  adxl.ActivityINT(1);
  adxl.FreeFallINT(1);
  adxl.doubleTapINT(1);
  adxl.singleTapINT(1);
}

void loop()
{
  int x,y,z, y_dash;
  adxl.readAccel(&x, &y, &z);
  y_dash = y-1;

  if(y_dash == 0) Serial.println("Level!");
  else if(y_dash > 0) Serial.println("Up a bit...");
  else if(y_dash < 0) Serial.println("Down a bit...");
  
  delay(1000);
}
