
#include <AFMotor.h>
#include <Stepper.h>
AF_Stepper crane(200, 2);              // Define Nombre del motor(# de pasos por vueltas, a la puerta M1 M2)
//AF_Stepper plate(200, 2);               // Define Nombre del motor(# de pasos por vueltas, a la puerta M3 M4)


void setup()
   {
      Serial.begin(9600);            // No importante
      crane.setSpeed(300);           // Define velocidad de giro en rpm
      //plate.setSpeed(1);           
   }

void loop() {
     crane.step(8000, BACKWARD, DOUBLE);    // Define (# de pasos a realizar, sentido de giro, método de giro (correspondiente al tipo de motor))
     delay(2000);
    // crane.step(200, BACKWARD, DOUBLE);
    
     //delay(2000);                         // Define tiempo de espera en milisegundos
     //plate.step(20, FORWARD, DOUBLE); 
     //plate.step(20, BACKWARD, DOUBLE);
     //delay(1000);


}
