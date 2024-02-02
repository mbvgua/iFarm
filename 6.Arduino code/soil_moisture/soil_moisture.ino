int readPin = A0;
int waitTime = 5000;
int readVal;
float actualVal;

void setup() {
  // put your setup code here, to run once:
  pinMode(readPin, INPUT);
  Serial.begin(9600);

}

void loop() {
  // before validation
  // readVal = analogRead(readPin);
  // Serial.println(readVal);
  // delay(waitTime);
  // when completely wet = (444 + 459 + 440)/3 =448 when completely dry = 1023 thus x *(100./448)

  readVal = analogRead(readPin);
  actualVal =(102300./575.)-readVal * (100./575.);
  Serial.print("This is the soil moisture content: ");
  Serial.println(actualVal);
  Serial.print("The uncalibrated readings are: ");
  Serial.println(readVal);
  delay(waitTime);
}
