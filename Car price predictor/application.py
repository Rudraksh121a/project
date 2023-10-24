from flask import Flask,render_template
import pandas as pd

app=Flask(__name__)
pd.read_csv("C:/Users/ram/Desktop/project/Car price predictor/Dataset/cleaned Car.csv")



@app.route('/')
def index():
    companies=sorted(car['company'].unique())
    car_models=sorted(car['name'].unique())
    year=sorted(car['year'].unique())
    fuel_type=sorted(car['fuel_type'].unique(),reverse=True)

    return render_template('index.html',companies=companies,car_models=car_models,years=year,fuel_type=fuel_type) 

if __name__=='__main__':
    app.run(debug=True)