// code with logic for pump and relay
int relayPin = 8; //initialize the signal pin for the relay
int moisturePin = A0;  //initialize thesignal pin for the moisture
int readMoistureVal;
float actualVal; 
// int thresHold; //declare variable threshold, above which pumps will turn off
int waitTime = 2000;

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
  
	if (actualVal <= 30.0 )
	{
    digitalWrite(relayPin, HIGH);
    Serial.print("The soil moisture content is: ");
    Serial.println(actualVal);
  	Serial.print(". The pump status is ON ");
  }
  else if(actualVal >= 30.1 && actualVal <= 70.0)
  {    
    Serial.print("The soil moisture content is: ");
    Serial.println(actualVal);
  	Serial.println(". This is sufficient for growth");
  }
	else if(actualVal >= 70.1)
  {
    digitalWrite(relayPin, LOW);
    Serial.print("The soil moisture content is: ");
    Serial.println(actualVal);
  	Serial.print(". The pump status is OFF");
	}
  else
  {
    Serial.println("There was an error!");

  }

	delay(waitTime);

}