#include <Wire.h>


#include "MAX30100.h"


MAX30100* pulseOxymeter;

void setup() {
  Wire.begin();
  Serial.begin(9600);
  Serial.println("Pulse oxymeter test!");

  pulseOxymeter = new MAX30100();
  pinMode(2, OUTPUT);

}

void loop() {
   
pulseoxymeter_t result = pulseOxymeter->update();
  
  if( result.pulseDetected == true )
  {
    Serial.println("LATIDOS");
    
    Serial.print( "BPM: " ); // latidos
    Serial.print( result.heartBPM );
    Serial.print( "SaO2: " ); // concentracion en sangre
    Serial.print( result.SaO2 );
    Serial.println( "%" );
  }
}
