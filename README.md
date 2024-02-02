# Automated irrigation project

In this project I will guide you through building an automated home irrigation system. For succesful completion of the project on your own, you would need the following components and tools:
+ **MCU** - I reccommend ESP8266 as it need to communicate over wifi, but you can use an Arduino Uno for prototyping
+ **Soil Moisture sensor** - a capacitive soil moisture sensor is advisable as its probes do not corrode overtime. However, I used a resisitive soil moisture sensor.
+ **Temperature sensor** - I used a DHT11 temperature sensor, that is also able to measure humidity. In this case however, I used it only for the former function.
+ **12V submersible Pump** - A 9V/5V pump would still do the same fnction effectively
+  **Relay** - 
+ **Basic programming skills** - allow you to program the MCU in simplified C++ and also build the interface using flask, a python framework.
 
Here i list down all the code that I employ to run my system. it has been categorised into the following sections:

1. Code to read temperature on DHT11 [here](2.TemeperatureSensor/temperature_sensor.md)
1. Code to read soil moisture sensor readings [here](1.SoilMoistureSensor/soil_moisture_sensor.md)
1. Code for the relay module [here](3.Relay/relay_code.md)
1. Code to merge the relay and the pump [here](4.Pump/pump.md)
1. Code that builds app dashboard in flask[here]()
1. Code to send data of both temp and moisture levels over wifi [here]()

------------
