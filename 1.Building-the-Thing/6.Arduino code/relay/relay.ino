int readPin = 8;
int waitTime = 2000;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(readPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(readPin, HIGH);
  Serial.println("The pump status is: ON!");
  delay(waitTime);
  digitalWrite(readPin, LOW);
  Serial.println("The pump status is: OFF!");
  delay(waitTime);
}

