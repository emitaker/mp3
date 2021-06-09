#include "DHT.h" // esto es para el sensor de temperatura
#define DHTTYPE DHT11   
const int DHTPin = 44;     
DHT dht(DHTPin, DHTTYPE);

int buttonState = 0;      
   
void setup()
{
  pinMode(30,INPUT_PULLUP);
  Serial.begin(9600);
  dht.begin();
}
void loop(){
  int y = 0;
  int joystickyaxispin = analogRead(A8); 
  int joystickxaxispin = analogRead(A9);

  //sensor de temperatura
  float t = dht.readTemperature();
  
  int mappedxaxis = map(joystickxaxispin + 18,0,1023,-6,5);
  int mappedyaxis = map(joystickyaxispin + 18,0,1023,-5,5);
  buttonState = digitalRead(30);

  Serial.println("Temp: ");
  Serial.println(t);
  delay(250);
  
  if(buttonState == LOW){
    Serial.println("pushed");
    delay(250);
  }
  else if(mappedxaxis == 5){
    Serial.println("right");
    delay(250);
  }
  else if(mappedxaxis == -5 || mappedxaxis == -6){
    Serial.println("left");
    delay(250);
  }
  else if(mappedyaxis == -1 || mappedyaxis == 0 || mappedyaxis == -2 || mappedyaxis == -4){
    Serial.println("nothing");
    delay(250);
  }
  else if(mappedyaxis == -5){
    Serial.println("up");
    delay(250);
  }
  else if(mappedyaxis==5 || mappedyaxis==6){
    Serial.println("down");
    delay(250);
  }
 
}
