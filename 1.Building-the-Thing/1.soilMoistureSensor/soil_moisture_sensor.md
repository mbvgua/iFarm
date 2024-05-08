### Soil moisture sensor code

I used a resisitive soil moisture sensor. That is depicted as below:
![Resisitive Soil Moisture Sensor](dht11_sensor.png)

It has two ends. The input and the ouput end. The input end has two pins that connect to the two resisitive probes on the sensor, registering the amount of resistence between them. The output end has 4 pins:

+ **VCC** this will be connected to the voltage pin, either 3V or 5V
+ **GND** this is connected to the ground pin
+ **DO** this is the digital read pin. We will not be using this pin.
+ **A0** this will be the analogue read pin. Arduino board will take input from this and display it on the serial monitor


Code to run the sensor is as below:

```C++
int readPin = A0;
int waitTime = 1000;
int readVal;
float actualVal;

void setup() {
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

The measured soil moisture is relative, ranging from 0 to 1023, and we need to do calibration to determine a threshold between wet and dry. While calibrating the sensor above, i found that when the sensor is completely dry its reads `1023`, which translates to `0%`. When completely immersed in water it reads (based on an average of 3) `448`, which is ` 100% `. This is used to build logic for my irrigation pump, to turn it on below a ceratin threshold. I used **30%** which is the best soil moisture content for maximum kale growth.

```C++
int readPin = A0;
int waitTime = 1000;
int readVal;
float actualVal;
int threshHold = 30;

void setup() {
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
