## 12V Pump

The 12V pump usually has two pins. 
+ A negative pin(-ve) - is black in colour. Needs to be connected to the GND of the power supply.
+ A positive pin(+ve) - is red in colour. Is connected to the 12V DC power supply.

![Relay pump](pump.png)

To controll the 12V pump, you would need an external power outlet, that is usually an adapter or connecting it to a live power source. Trying to connect the pump to the MCU directly to controll it would in turn burn it up due to the high power demand. We instead employ a relay module. Relays are vital for controlling devices that have power requirements of more than 5V.

```C++
int relayPin = 8;
int waitTime = 2000;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(relayPin, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(relayPin, HIGH);
  Serial.println("The pump status is: ON!");
  delay(waitTime);
  digitalWrite(relayPin, LOW);
  Serial.println("The pump status is: OFF!");
  delay(waitTime);
}

```
