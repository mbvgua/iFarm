# Automated irrigation project :herb:

In this project I will guide you through building an automated home irrigation system. For successful completion of the project on your own, you would need the following components and tools:
+ **MCU** - I reccomend an ESP8266 microcontroller as it is needed to communicate over wifi, but you can use an Arduino Uno for basic prototyping
+ **Soil Moisture sensor** - a capacitive soil moisture sensor is advisable as its probes do not corrode overtime. However, I used a resisitive soil moisture sensor as it was readily available.
+ **Temperature sensor** - I used a DHT11 temperature sensor, that is also able to measure humidity. In this case however, I used it only for the former function.
+ **12V submersible Pump** - A 9V/5V pump would still do the same fnction effectively
+  **Relay** - to be able to controll the submersible pump using my MCU and avoid burning it out, i needed a relay that would act as the switch.
+ **Basic programming skills** - allow you to program the MCU in simplified C++ and also build the interface using flask, a python framework.

Here i list down all the code that I employ to run my system. it has been categorised into the following sections:

1. Code to read temperature on DHT11 [here](1.Building-the-Thing/2.temeperatureSensor/temperature_sensor.md)
1. Code to read soil moisture sensor readings [here](1.Building-the-Thing/1.soilMoistureSensor/soil_moisture_sensor.md)
1. Code for the relay module [here](1.Building-the-Thing/3.Relay/relay_code.md)
1. Finalized Arduino Code, with the Firebase database logic include [here](1.Building-the-Thing/6.finalCode)
1. Understanding how to use the webapp [here](3.Building-the-Website/README.md)


------------
