from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from .models import Report
from . import db as database
# from firebase import firebase
import firebase_admin
from firebase_admin import db  # credentials
import numpy as np
import pandas as pd
from joblib import dump, load
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import uuid
import kaleido

views = Blueprint('views', __name__)


# register your firebase application
cred = firebase_admin.credentials.Certificate(
    'website/static/esp8266-moisture-a515b-firebase-adminsdk-787qf-cb4320fc63.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://esp8266-moisture-a515b-default-rtdb.firebaseio.com/'
})

# linear regression code
dataset = 'website/static/nyeri_kales_dataset2.csv'
path_str = uuid.uuid4().hex
image = 'static/images/' + path_str + '.svg'
image_path = 'website/' + image

model = load('website/static/lr_model.joblib')
data = pd.read_csv(dataset)

drop_columns = ['Humidity_Level', 'Soil_Type', 'Daily_Precipitation_mm', 'Sunlight_Duration_hrs']
df = data.drop(drop_columns, axis=1)

X = df.drop('GDD', axis=1)
y = df['GDD']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=17)

lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)

plt.figure(figsize=(12, 6))
plt.scatter(y_test, y_pred, label='Predicted GDD based on Min and Max temperatures')
x_line = [min(y_test), max(y_test)]
y_line = [min(y_test), max(y_test)]
plt.plot(x_line, y_line, linestyle='--', color='red', linewidth=2, label='Target(GDD)')
plt.title("Linear Regression Graph of predicted GDD")
plt.xlabel("Min and Max Temperatures")
plt.ylabel("GDD")
plt.legend()
plt.grid(True)
plt.savefig(image_path)
plt.show()
plt.close()  # Close the figure to avoid memory leaks



@views.route('/', methods=['GET', 'POST'])
@login_required
def index():
    """ function for all the logic in the homepage"""

    return render_template('index.html',user=current_user)


@views.route('/model', methods=['GET', 'POST'])
@login_required
def model():
    if request.method == 'POST':
        # Get a reference to the desired data location
        max_temp_ref = db.reference('ambientTemperature/maxTemp')
        min_temp_ref = db.reference('ambientTemperature/minTemp')

        # Fetch the data
        try:
            max_temp_list = max_temp_ref.get()
            min_temp_list = min_temp_ref.get()
        except Exception as e:
            return f"Error retrieving data: {e}"

        # get the maximum and minimum values from dictionary of values
        maxTemp = float(max(max_temp_list.values()))
        minTemp = float(min(min_temp_list.values()))

        def make_prediction():
            # save the dataset into a dictionary
            new_vals = {'Max_Temperature_C': maxTemp, 'Min_Temperature_C':minTemp}

            # convert data into a dataframe
            new_data = pd.DataFrame(new_vals, index=[0])

            # make the prediction
            preds = int(lr.predict(new_data))
            return preds

        prediction = make_prediction()

        # report = f'{ current_user.username }. Based on the application, your plant experinced maximum temperatures of {maxTemp} and minimum temperatures of {minTemp}. Based on our prediction model, it experienced a total of {prediction} Growing Degree Days.'
        val = lambda x: x if bool(x) else 'Undefined'
        report = f'{ current_user.username }. Based on the application, your plant experinced maximum temperatures of {val(maxTemp)} and minimum temperatures of {val(minTemp)}. Based on our prediction model, it experienced a total of {prediction} Growing Degree Days.'
        message = 'Your report has been added'
        flash(message, category='success')

        new_report = Report(data=report, user_id=current_user.id)
        database.session.add(new_report)
        database.session.commit()

        return render_template ('model_page.html', user=current_user,image=image, prediction=prediction,maxTemp=maxTemp,minTemp=minTemp)

    return render_template('model_page.html', user=current_user,image=image)#, prediction=prediction, maxTemp=maxTemp,minTemp=minTemp)
