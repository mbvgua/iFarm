console.log('begin execution')

const firebaseConfig = {
    apiKey: "AIzaSyCpwFROlZwW4l4ZNJhz_JqeSE8ovQaSiew",
    authDomain: "esp8266-moisture-a515b.firebaseapp.com",
    databaseURL: "https://esp8266-moisture-a515b-default-rtdb.firebaseio.com",
    projectId: "esp8266-moisture-a515b",
    storageBucket: "esp8266-moisture-a515b.appspot.com",
    messagingSenderId: "10946572396",
    appId: "1:10946572396:web:d4eb7ba251e8389762a849"
};

console.log('Succesfully sent the config SDK')

// initialize the firebase app
firebase.initializeApp(firebaseConfig);
console.log('Initialize the firebase app')

// create a adatabase reference
const db = firebase.database();
console.log('Initialize the firebase database')

// reference the value that youd like to change
const relayVal = db.ref('relayControll/status')
const maxTemp = db.ref('ambientTemperature/maxTemp')
const minTemp = db.ref('ambientTemperature/minTemp')
const soilMoisture = db.ref('soilMoistureContent/valueAsPercentage')
console.log("database references acquired");


// Get the checkbox element
var relayControllCheckbox = document.getElementById('relayControll');
var relayState = document.getElementById('relayState');
var maxTempVal = document.getElementById('maxTemp');
var minTempVal = document.getElementById('minTemp');
var soilMoistureVal = document.getElementById('soilMoisture');
console.log("id elements reference acquired");

//
relayControllCheckbox.addEventListener('change', function(){
    const newState = this.checked ? 'ON' : 'OFF';
    relayVal.set(newState)
    .then(() => {
        console.log(`Relay state set to: ${newState}`);
    })
    .catch((error) => {
        console.log('Error writing data:', error);
    })

})

// function to display max value dynamically
maxTemp.on('value', function(snapshot) {
  var data = snapshot.val();
  // Display the data on your web app using data
    console.log(`${data}`)
    // maxTempVal.innerHTML =  data;    //display [Object]
    // maxTempVal.innerHTML =  Object.values(data).pop();  //display the last added value in {key:values}
    maxTempVal.innerHTML =  Math.max(...Object.values(data));  //display the HIGHEST  value in {key:values}. MUST ADD ... otherwise will return NaN
    console.log(`The max temp is : ${maxTempVal.innerHTML}`)
});

// function to display min value dynamically
minTemp.on('value', function(snapshot) {
  var data = snapshot.val();
  // Display the data on your web app using data
    console.log(`${data}`)
    // minTempVal.innerHTML =  Object.values(data).pop();  //display the last added value in {key:values}
    minTempVal.innerHTML =  Math.min(...Object.values(data));  //display the highest value in {key:values}. MUST ADD ... otherwise will return NaN
    console.log(`The min temp is : ${minTempVal.innerHTML}`)
});

// function to display soil moisture content dynamically
soilMoisture.on('value', function(snapshot) {
  var data = snapshot.val();
  // Display the data on your web app using data
  console.log(`${data}`)
  soilMoistureVal.innerHTML =  data;
});

// function to display relay state
relayVal.on('value', function(snapshot) {
  var data = snapshot.val();
  // Display the data on your web app using data
  console.log(`${data}`)
  relayState.innerHTML =  data;
});







// displaying data onto your web page

// // function to read the data
// function displayData(){

//     .then(() => {
//         console.log('data displayed succesfully')
//     })
//     .catch((error) => {
//         console.log('Error displaying data :', error):
//     })
// }
