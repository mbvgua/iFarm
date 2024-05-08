/*
  Make sure your Firebase project's '.read' and '.write' rules are set to 'true'. 
  Ignoring this will prevent the MCU from communicating with the database. 
  For more details- https://github.com/Rupakpoddar/ESP8266Firebase 
*/
#include <ArduinoJson.h>            // https://github.com/bblanchon/ArduinoJson 
#include <ESP8266Firebase.h>
#include <ESP8266WiFi.h>
#include <DHT11.h>


// #define WIFI_SSID "dekut"        // Your WiFi SSID
// #define WIFI_PASSWORD "dekut@ict2023"      // Your WiFi Password
#define WIFI_SSID "GWANGIS"
#define WIFI_PASSWORD "lastofus" 
#define REFERENCE_URL "https://esp8266-moisture-a515b-default-rtdb.firebaseio.com/"  // Your Firebase project reference url


Firebase firebase(REFERENCE_URL);

//define your variables
int moisturePin = A0; //OR 
int waitTime = 200;
int readVal;
float actualVal;
int temperature;
int tempPin = D0; //OR 
int relayPin = D7;  //OR 13
String relayStatus = "";

DHT11 dht11(tempPin);

void setup() {
  Serial.begin(115200);
  pinMode(moisturePin, INPUT);
  pinMode(relayPin, OUTPUT);
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  // delay(waitTime);

  // Connect to WiFi
  Serial.println();
  Serial.println();
  Serial.print("Connecting to: ");
  Serial.println(WIFI_SSID);
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print("-");
  }

  Serial.println("");
  Serial.println("WiFi Connected!!!");

  // Print the IP address
  Serial.print("IP Address: ");
  Serial.print("http://");
  Serial.print(WiFi.localIP());
  Serial.println("/");
   
}

void loop() {

  readVal = analogRead(moisturePin);
  actualVal =(102300./575.)-readVal * (100./575.);
  Serial.print("This is the soil moisture content: ");
  Serial.println(actualVal);

  // Attempt to read the temperature value from the DHT11 sensor.
  temperature = dht11.readTemperature();

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


  // LED/ RELAY CONTROLL LOGIC
  relayStatus = firebase.getString("relayControll/status");

  if (relayStatus == "ON" ) {
    digitalWrite(relayPin, HIGH);
    Serial.println("Relay turned ON");
  }
  else if ( relayStatus == "OFF" ) {
    digitalWrite(relayPin, LOW);
    Serial.println("Relay turned OFF");
  }
  else {
    Serial.println("Wrong Credentials. Input either ON/OFF");
  }
  
  Serial.println(".");
  Serial.println(".");
  Serial.println(".");

  
  //push soil moisture value
  // firebase.pushInt("soilMoistureVal", actualVal);   //does not work since value maybe 0.sth
  //set float value unstead


  // // code snippet to automate the irrigation process
  // 	if (actualVal <= 30.0 )
	// {
  //   digitalWrite(relayPin, HIGH);
  //   firebase.setString("relayControll/status", "ON");
  //   Serial.print("The soil moisture content is: ");
  //   Serial.println(actualVal);
  // 	Serial.print(". The pump status is ON ");
  // }
  // else if(actualVal >= 30.1 && actualVal <= 70.0)
  // {    
  //   firebase.setString("relayControll/status", "OFF");
  //   Serial.print("The soil moisture content is: ");
  //   Serial.println(actualVal);
  // 	Serial.println(". This is sufficient for growth");
  // }
	// else if(actualVal >= 70.1)
  // {
  //   digitalWrite(relayPin, LOW);    
  //   Serial.print("The soil moisture content is: ");
  //   Serial.println(actualVal);
  // 	Serial.print(". The pump status is OFF");
	// }
  // else
  // {
  //   Serial.println("There was an error!");

  // }


  // firebase.setString("relayControll/status", relayStatus);
  firebase.setFloat("soilMoistureContent/valueAsPercentage", actualVal);
  firebase.pushFloat("ambientTemperature/maxTemp", temperature);
  firebase.pushFloat("ambientTemperature/minTemp", temperature);

  // Example of getting an int.
  // float soilMoistureVal = firebase.getFloat("soilMoisture/percentageValue");
  // Serial.print("Received Float:\t\t");
  // Serial.println(soilMoistureVal);

  // Example of getting an int.
  // int maxTemp = firebase.getInt("ambientTemperature/maxTemp");
  // Serial.print("Received Int:\t\t");
  // Serial.println(maxTemp);

  // Example of getting an int.
  // float minTemp = firebase.getFloat("ambientTemperature/minTemp");
  // float maxTemp = firebase.getFloat("ambientTemperature/maxTemp");
  // Serial.print("Received Float:\t\t");
  // Serial.println(minTemp);
  // Serial.println(maxTemp);

  delay(waitTime);
} 