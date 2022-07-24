//Carlos Jesus Garcia Cano 20/07/2022
const int but1 = 5;
const int  but2 = 6;
const int but3 = 4;
const int but4 = 3;

void setup() 
{
  Serial.begin(9600);
  pinMode(but1,INPUT);
  pinMode(but2,INPUT);
  pinMode(but3,INPUT);
  pinMode(but4,INPUT);
  Serial.println(0);
}

void loop()
{
  if(digitalRead(but1) == HIGH)
  {
    Serial.println(1);
    digitalWrite(but1,LOW) ;
    delay(50);
    }
  if(digitalRead(but2) == HIGH)
  {
    Serial.println(2);
    digitalWrite(but2,LOW) ;
    delay(50);
    }
  if(digitalRead(but3) == HIGH)
  {
    Serial.println(3);
    digitalWrite(but3,LOW) ;
    delay(50);
    }
  if(digitalRead(but4) == HIGH)
  {
    Serial.println(4);
    digitalWrite(but4,LOW) ;
    delay(50);
    }
  else{
    Serial.println(0);
    
    delay(50);
    
    }
}
