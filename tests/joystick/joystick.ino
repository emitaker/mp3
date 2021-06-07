int buttonState = 0;         

void setup()
{
  pinMode(7,INPUT_PULLUP);
  Serial.begin(9600);
}
void loop(){
  int y = 0;
  int joystickyaxispin = analogRead(A8); 
  int joystickxaxispin = analogRead(A9);
  int mappedxaxis = map(joystickxaxispin + 18,0,1023,-6,5);
  int mappedyaxis = map(joystickyaxispin + 18,0,1023,-5,5);
  buttonState = digitalRead(0);
  
  if(buttonState == LOW){
    Serial.println("pushed");
    delay(80);
  }
  else if(mappedxaxis == 5){
    Serial.println("right");
    delay(80);
  }
  else if(mappedxaxis == -5 || mappedxaxis == -6){
    Serial.println("left");
    delay(80);
  }
  else if(mappedyaxis == -1 || mappedyaxis == 0 || mappedyaxis == -2 || mappedyaxis == -4){
    Serial.println("nothing");
    delay(80);
  }
  else if(mappedyaxis == -5){
    Serial.println("up");
    delay(80);
  }
  else if(mappedyaxis==5 || mappedyaxis==6){
    Serial.println("down");
    delay(80);
  }
 
}
