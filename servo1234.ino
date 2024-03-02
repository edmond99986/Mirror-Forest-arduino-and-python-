#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// called this way, it uses the default address 0x40
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();
// you can also call it with a different address you want
//Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x4F);

// Depending on your servo make, the pulse width min and max may vary, you 
// want these to be as small/large as possible without hitting the hard stop
// for max range. You'll have to tweak them as necessary to match the servos you
// have!
// Watch video V1 to understand the two lines below: http://youtu.be/y8X9X10Tn1k
#define SERVOMIN  125 // this is the 'minimum' pulse length count (out of 4096)
#define SERVOMAX  575 // this is the 'maximum' pulse length count (out of 4096)

// our servo # counter
uint8_t servonum = 0;
char val;
String pos;
int x;
int y;

void setup() {
  Serial.begin(115200);
  
  
  Serial.setTimeout(3);

  pwm.begin();
  
  pwm.setPWMFreq(40);  // Analog servos run at ~60 Hz updates

  yield();
}

// the code inside loop() has been updated by Robojax
void loop() {
while (!Serial.available());
    /* int ang= ValToAngle(val);*/
     pos = Serial.readString();
     y = pos.toInt();
     x= map(y,0,1280,10,450);
     pwm.setPWM(0, 0, x);
     pwm.setPWM(1,0,x );
     pwm.setPWM(2, 0, x );
     pwm.setPWM(3,0, x);
     pwm.setPWM(4, 0, x );
     pwm.setPWM(5,0,x );
     pwm.setPWM(6, 0,x );
     pwm.setPWM(7,0,x);
     pwm.setPWM(8, 0, x);
     pwm.setPWM(9,0,x );
     pwm.setPWM(10, 0, x );
     pwm.setPWM(11,0, x);
     pwm.setPWM(12, 0, x );
     pwm.setPWM(13,0,x );
     pwm.setPWM(14, 0,x );
     pwm.setPWM(15,0,x);
     
    //delay(50);// wait for 1 second


}


/*
/* angleToPulse(int ang)
 * @brief gets angle in degree and returns the pulse width
 * @param "ang" is integer represending angle from 0 to 180
 * @return returns integer pulse width
 * Usage to use 65 degree: angleToPulse(65);
 * Written by Ahmad Shamshiri on Sep 17, 2019. 
 * in Ajax, Ontario, Canada
 * www.Robojax.com 
 */
 
