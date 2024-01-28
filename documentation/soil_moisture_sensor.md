### Soil moisture sensor code

I used a resisitive soil moisture sensor. It comes with 4 pins:

+ <mark>VCC</mark> this will be connected to the voltage pin, either 3V or 5V
+ <mark>GND</mark> this is connected to the ground pin
+ <mark>A0</mark> this will be the read pin. Arduino board will take input from this and display it on the serial monitor
+ <mark></mark>

code to run the sensor is as below:

```C++
int readPin = A0;
int waitTime = 1000;
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
  Serial.println(readVal);
  delay(waitTime);
}
```

The measured soil moisture is relative, ranging from 0 to 1023, and we need to do calibration to determine a threshold between wet and dry. While calibrating the sensor above, i found that when the sensor is completely dry its reads `1023`, which translates to `0%`. When completely immersed in water it reads an average of `448`, which is ` 100% `. This is used to build logic for my irrigation pump.

```C++
int readPin = A0;
int waitTime = 1000;
int readVal;
float actualVal;
int threshHold ;

void setup() {
  // put your setup code here, to run once:
  pinMode(readPin, INPUT);
  Serial.begin(9600);

}

void loop() {
  readVal = analogRead(readPin);
  actualVal =(102300./575.)-readVal * (100./575.);
  Serial.print("This is the soil moisture content: ");
  delay(waitTime);
  if actualVal >= threshHold {
    Serial.println("The soil moisture is above the threshold, pump status is off!")
  }
  else if threshHold >= actualVal {
    Serial.println("The soil moisture is below the threshold, pump status is on")
  }
}
}
```
