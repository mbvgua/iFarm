from flask import Flask, render_template, redirect, request
import sqlite3
import csv

# turn your file into a web app
app = Flask(__name__)


# # Begin working on the model functionality
# model_file = 'static/linear_regression_model.pkl'
# try:
#     model = load_model(model_file)
    
# except Exception as e:
#     print(f"Error loading the model: {e}")

# def load_model(model_filename):
#     with open(model_file, 'rb') as file:
#         model = pickle.load(file)
#     return model

# def predict_gdd(max_temp,min_temp,):   
#     prediction = model.predict([[max_temp, min_temp]])
#     return round(prediction[0], 2)


# listen to get requests for index
@app.route('/',methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/register')
def register():
	name = request.form.get("")
	return render_template('register.html')

@app.route('/forgot_password')
def forgot_password():
	return render_template('forgot_password.html')



