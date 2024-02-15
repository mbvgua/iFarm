#include <DHT11.h>
// code with logic for pump and relay
int relayPin = 8; //initialize the signal pin for the relay
int tempPin = 10;
int moisturePin = A0;  //initialize thesignal pin for the moisture
int readMoistureVal;
float actualVal; 
// int thresHold; //declare variable threshold, above which pumps will turn off
int waitTime = 2000;
DHT11 dht11(tempPin);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);
  pinMode(moisturePin, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  readMoistureVal = analogRead(moisturePin);
  actualVal =(102300./575.)-readMoistureVal * (100./575.);
  // Serial.println(actualVal);
  int temperature = dht11.readTemperature();
  Serial.print("Temperature: ");
  Serial.print(temperature);
  Serial.println(" °C");


	if (actualVal <= 30.0 )
	{
    digitalWrite(relayPin, HIGH);
    Serial.print("The soil moisture content is: ");
    Serial.println(actualVal);
  	Serial.println(". The pump status is ON ");
    Serial.println('*');
    Serial.println('*');
    Serial.println('*');
  }
  else if(actualVal >= 30.1 && actualVal <= 70.0)
  {    
    Serial.print("The soil moisture content is: ");
    Serial.println(actualVal);
  	Serial.println(". This is sufficient for growth");
    Serial.println('*');
    Serial.println('*');
    Serial.println('*');
  }
	else if(actualVal >= 70.1)
  {
    digitalWrite(relayPin, LOW);
    Serial.print("The soil moisture content is: ");
    Serial.println(actualVal);
  	Serial.println(". The pump status is OFF");
    Serial.println('*');
    Serial.println('*');
    Serial.println('*');
	}
  else
  {
    Serial.println("There was an error!");

  }

	delay(waitTime);

}