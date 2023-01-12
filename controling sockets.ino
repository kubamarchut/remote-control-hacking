/*
  Example for different sending methods
  
  https://github.com/sui77/rc-switch/
  
*/

#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

void setup() {

  Serial.begin(9600);
  
  // Transmitter is connected to Arduino Pin #10  
  mySwitch.enableTransmit(10);
  
  // Optional set protocol (default is 1, will work for most outlets)
  // mySwitch.setProtocol(2);

  // Optional set pulse length.
  mySwitch.setPulseLength(170);
  
  // Optional set number of transmission repetitions.
  // mySwitch.setRepeatTransmit(15);
  
}

void loop() {  
  mySwitch.send(1332531, 24);
  delay(1000);  
  mySwitch.send(1332675, 24);
  delay(1000);
  mySwitch.send(1332540, 24);
  delay(1000); 
  mySwitch.send(1332684, 24);  
  delay(1000);
  /* not used buttons 5 and 6
  mySwitch.send(1332995, 24);
  delay(1000); 
  mySwitch.send(1333004, 24);
  delay(1000); 
  */
  delay(2000);
}
