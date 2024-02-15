
// Include the DHT11 library for interfacing with the sensor.
#include <DHT11.h>

// Create an instance of the DHT11 class.
// - For Arduino: Connect the sensor to Digital I/O Pin 2.
// - For ESP32: Connect the sensor to pin GPIO2 or P2.
// - For ESP8266: Connect the sensor to GPIO2 or D4.
int readPinDH = 2;
DHT11 dht11(readPinDH);

// soil moisture
int readPinSM = A0;
int waitTime = 1000;
int readVal;
float actualVal;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(readPinDH, INPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  // Attempt to read the temperature value from the DHT11 sensor.
  int temperature = dht11.readTemperature();

  // Check the result of the reading.
  // If there's no error, print the temperature value.
  // If there's an error, print the appropriate error message.
  if (temperature != DHT11::ERROR_CHECKSUM && temperature != DHT11::ERROR_TIMEOUT)
  {
      Serial.print("Temperature: ");
      Serial.print(temperature);
      Serial.println(" °C");
  }
  else
  {
      Serial.println(DHT11::getErrorString(temperature));
  }

  readVal = analogRead(readPinSM);
  actualVal =(102300./575.)-readVal * (100./575.);
  Serial.print("This is the soil moisture content: ");
  Serial.println(actualVal);
  Serial.print("The uncalibrated readings are: ");
  Serial.println(readVal);
  delay(waitTime);
    // Wait for 1 seconds before the next reading.
    delay(waitTime);
}
