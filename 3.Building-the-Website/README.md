<!-- create the get back to top link -->
<a name="readme-top"></a>

# **iFarm :seedling:** 

iFarm project was built and completed while doing my final year. It is intended for learning purposes taking on a hands-on approach of learning by doing. Everything was built from scratch by myself with the notable contribution of individuals mentioned in the acknowledgements. 


<!-- TABLE OF CONTENTS IN MARKDOWN -->
### TABLE OF CONTENTS
1. [Introduction](#introduction)
1. [Getting started](#getting-started)
1. [Contributing](#contributing)
1. [Contact](#contact)
1. [Acknowledgments](#acknowledgments)
1. [License](#license)


 ### Introduction :trident:

 iFarm is a 3-tier automated irrigation system. It has 4 main components:
  - The IoT devices intended to collect, transmit and regulate data on the farm
  - Firebase RTDB :- the web hosted realtime NoSQL database
  - The web application :- primarily built in flask for the backend and a dash of javascript. It also houses the AI model built entirely in python.

Images for various functional components of the application can be found in [assets](../assets/) in the appropriate chronological order

 ### Getting started :hammer:

 The project will need an installation of flask. You can confirm this by inputing the following command onto your terminal, and inside the virtual environment, check whether you have an installed version:

 * for Flask
   ```sh

    $ source .flaskVenv/bin/activate
    (.flaskVenv) $ python -m flask --version
    # -> Python 3.10.14
    # -> Flask 3.0.3
    # -> Werkzeug 3.0.2

   ```

   > Remember that its is always a good practice develop in a virtual environment to prevent possible breakage with future updates.


 Now that you have the main dependencies installed locally, you can download the repository and run the desired project.

 1. Clone the repo
    ```bash
    git clone https://github.com/your_username_/Automated-Irrigation-System-Using-an-MCU.git
    ```
 2. Navigate to the project folder
    ```bash
    cd Automated-Irrigation-System-Using-an-MCU/3.Building-the-Website
    ```
 3. Install the needed requirements located in the `requirements.txt` file
    ```bash
    pip install -r requirements.txt
    ```

 4. Navigate to the main website repository
    ```bash
    cd iFarm
    ```
 5. Run the desired project.
    ```bash
    python app.py
    ```

 <p align="right">(<a href="#readme-top">back to top</a>)</p>


 <!-- CONTRIBUTING -->
 ## Contributing :speech_balloon:

 Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are much appreciated.

 If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
 Don't forget to give the project a star!

 1. Fork the Project
 2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
 3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
 4. Push to the Branch (`git push origin feature/AmazingFeature`)
 5. Open a Pull Request

 For more information, you can check out [CONTRIBUTING.md](../.github/CONTRIBUTING.md)

 <p align="right">(<a href="#readme-top">back to top</a>)</p>


 <!-- CONTACT -->
 ## Contact :telephone:

 To contact me, Kindly raise an issue within the project repo and I will respond as soon as I can.

 <p align="right">(<a href="#readme-top">back to top</a>)</p>


 <!-- ACKNOWLEDGMENTS -->
 ## Acknowledgments :paperclip:
 > Standing on the shoulder of giants.

 Here I list all the noteworthy individuals and materials that helped me to see this idea to completion. Feel free to check them out too.

 * [Jeremiah Kiarie](https://github.com/jeremiahKiarie)
 * [Microsoft IoT-For-Beginners](https://github.com/microsoft/IoT-For-Beginners)
 * [Flask Documentation](https://flask.palletsprojects.com/en/3.0.x/)
 * [Firebase Documentation](https://firebase.google.com/docs/reference/js/database.md?_gl=1*7o0e0o*_up*MQ..*_ga*MjA4MjQ2MjIzMi4xNzI4ODA5ODc0*_ga_CW55HF8NVT*MTcyODgwOTg3NC4xLjAuMTcyODgwOTg3NC4wLjAuMA..#database_package)

 <p align="right">(<a href="#readme-top">back to top</a>)</p>


 <!-- LICENSE -->
 ## License :mag:

 Distributed under the GNU v3 Public License. See [LICENSE](../.github/LICENSE.txt) for more information.

 <p align="right">(<a href="#readme-top">back to top</a>)</p>
